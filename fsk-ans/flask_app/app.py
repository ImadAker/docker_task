from flask import Flask
import psutil
import mysql.connector
import json
app = Flask(__name__)
config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'stats'
}
@app.route('/cpu usage',methods=['GET'])
def cpu_usage():
    connection=mysql.connector.connect(**config)
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM cpu_percentage')
    pr = [percentage for percentage in cursor]
    cursor.close()
    connection.close()
    strg="Percentage\t\tDate\r<br/>"
    if len(pr) <24:
        for i in reversed(pr):
            strg+=i[0]+"\t"+i[1]+"\r<br/>"
        return strg
    c=0
    for i in reversed(pr):
        c+=1
        if(c>=24):
                break
        strg+=i[0]+"\t"+i[1]+"\r<br/>"

    return strg
@app.route('/mem usage',methods=['GET'])
def mem_usage():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM mem_percentage')
    pr = [percentage for percentage in cursor]
    cursor.close()
    connection.close()
    strg="Percentage\t\tDate\r<br/>"
    if len(pr) <24:
        for i in reversed(pr):
            strg+=i[0]+"\t"+i[1]+"\r<br/>"
        return strg
    c=0
    for i in reversed(pr):
        c+=1
        if(c>=24):
                break
        strg+=i[0]+"\t"+i[1]+"\r<br/>"

    return strg

@app.route('/disk usage',methods=['GET'])
def hdd_usage():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM disk_percentage')
    pr = [percentage for percentage in cursor]
    cursor.close()
    connection.close()
    strg="Percentage\t\tDate\r<br/>"
    if len(pr) <24:
        for i in reversed(pr):
            strg+=i[0]+"\t"+i[1]+"\r<br/>"
        return strg
    c=0
    for i in reversed(pr):
        c+=1
        if(c>=24):
                break
        strg+=i[0]+"\t"+i[1]+"\r<br/>"

    return strg

@app.route('/current cpu usage',methods=['GET'])
def current_cpu():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cpu_percentage')
    pr = [percentage for percentage in cursor]
    cursor.close()
    connection.close()
    #rev=reversed(pr)
    strg="Percentage\t\tDate\r<br/>"
    strg+=pr[-1][0]+"\t"+pr[-1][1]+"\r<br/>"
    return strg

@app.route('/current mem usage',methods=['GET'])
def current_mem():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM mem_percentage')
    pr = [percentage for percentage in cursor]
    cursor.close()
    connection.close()
    #rev=reversed(pr)
    strg="Percentage\t\tDate\r<br/>"
    strg+=pr[-1][0]+"\t"+pr[-1][1]+"\r<br/>"
    return strg

@app.route('/current disk usage',methods=['GET'])
def current_disk():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM disk_percentage')
    pr = [percentage for percentage in cursor]
    cursor.close()
    connection.close()
    #rev=reversed(pr)
    strg="Percentage\t\tDate\r<br/>"
    strg+=pr[-1][0]+"\t"+pr[-1][1]+"\r<br/>"
    return strg

if __name__ == '__main__':

    app.run(host='0.0.0.0')


