FROM centos:7

RUN yum install -y python3 python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN yum group install -y  "Development Tools"
RUN yum install -y man-pages
RUN yum install -y python3-devel
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
