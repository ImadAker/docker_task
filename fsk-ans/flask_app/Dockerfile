FROM centos:7

RUN yum install -y python3 python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt

RUN touch /var/log/performance.log

WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
