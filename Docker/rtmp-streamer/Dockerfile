FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y software-properties-common  wget ffmpeg curl
RUN apt-get -y install python3 python3-pip supervisor gunicorn
RUN apt install -y ffmpeg libswscale-dev libavcodec-dev

COPY ./python_requirements.txt /var/www/html/liveLinearStreamer/
WORKDIR /var/www/html/liveLinearStreamer
RUN pip3 install -r python_requirements.txt