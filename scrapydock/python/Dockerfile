ARG PYTHON_VERSION=latest
FROM python:${PYTHON_VERSION}
RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get install -y openssh-server
RUN apt-get install -y zlib1g-dev libffi-dev libssl-dev
RUN apt-get install -y libxml2-dev libxslt1-dev
RUN pip install setuptools
RUN pip install Scrapy
RUN apt-get install wget
RUN apt-get install vim
