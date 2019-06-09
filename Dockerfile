# Docker image for running examples in SummaryHelp API Server

# 1. server 환경을 위한 ubuntu 설치

FROM ubuntu:16.04

MAINTAINER Jungchaemoon <jungchaemoon@gmail.com>

RUN apt-get -y update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    python3-dev \
    python3-pip \
    python3-venv
    python-setuptools

# 2. nginx config file
EXPOSE 80
RUN apt-get install -y nginx
ADD /etc/nginx/sites-enabled/summary_nginx.conf /etc/nginx/sites-enabled/summary_nginx.conf

# 3. mysql server config file
EXPOSE 3306
RUN apt-get install mysql-server
ADD /etc/mysql/conf.d/default.cnf /etc/mysql/conf.d/default.cnf


# 4. API Server 사용을 위한 git clone

RUN git clone https://github.com/summaryhelpex/SummaryHelp_APIServer.git

RUN cd SummaryHelp_APIServer
RUN pip install -r requirements.txt

# 5. daemon 으로 돌리기위한 gunicorn configfile

ADD /etc/systemd/system/gunicorn.service /etc/systemd/system/gunicorn.service