from flask import Flask
import mysql.connector
import logging
app = Flask(__name__)
config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'stats'
}
logging.basicConfig(filename="/var/log/performance.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
def func_logger(func):
    def inner(*args):
        ret=func(*args)
        logger.info(f'Call function {func.__name__} with {args}')
        return ret
    return inner

@func_logger
def get_usages(sel):
    connection=mysql.connector.connect(**config)
    cursor=connection.cursor()
    query=f"SELECT * FROM {sel}_percentage ORDER BY time desc limit 24"
    cursor.execute(query)
    pr = [percentage for percentage in cursor]
    cursor.close()
    connection.close()
    strg="Percentage\t\tDate\r<br/>"
    for i in pr:
        strg+=i[0]+"\t"+i[1]+"\r imad <br/>"
    return strg

@func_logger
def get_current_usages(sel):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query=f"SELECT * FROM {sel}_percentage ORDER BY time DESC  limit 1"
    cursor.execute(query)
    pr = [percentage for percentage in cursor]
    cursor.close()
    connection.close()
    #rev=reversed(pr)
    strg="Percentage\t\tDate\r<br/>"
    strg+=pr[0][0]+"\t"+pr[0][1]+"\r<br/>"
    return strg
 
 
@app.route('/cpu usage',methods=['GET'])
def cpu_usage():
    return get_usages("cpu")
@app.route('/mem usage',methods=['GET'])
def mem_usage():
    return get_usages("mem")
@app.route('/disk usage',methods=['GET'])
def hdd_usage():
    return get_usages("disk")

@app.route('/current cpu usage',methods=['GET'])
def current_cpu():
    return get_current_usages("cpu")
@app.route('/current mem usage',methods=['GET'])
def current_mem():
    return get_current_usages("mem")

@app.route('/current disk usage',methods=['GET'])
def current_disk():
    return get_current_usages("disk")

if __name__ == '__main__':

    app.run(host='0.0.0.0')


