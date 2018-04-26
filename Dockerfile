FROM ubuntu:xenial

RUN \
 apt-get update \
 && apt-get install -y software-properties-common python-software-properties apt-transport-https \
 && add-apt-repository ppa:jonathonf/python-3.6 \
 && apt-get update \
 && apt-get install -y build-essential python3.6 python3.6-dev gdal-bin curl

# Cleanup apt files so that image size is smaller.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ARG DEBIAN_FRONTEND=noninteractive

ENV PYTHONUNBUFFERED 1
RUN mkdir /project
WORKDIR /project
# Installing all requirements
ADD requirements.txt /project
RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6
RUN python3.6 -m pip install -r requirements.txt
# Expose port
EXPOSE 5444
ADD . /project
