FROM ubuntu:latest
MAINTAINER Ben Weber

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install pandas \
  && pip3 install sklearn \
  && pip3 install pandas_gbq
  
COPY pipeline.py pipeline.py
COPY dsdemo.json dsdemo.json

RUN export GOOGLE_APPLICATION_CREDENTIALS=/dsdemo.json

ENTRYPOINT ["python3", "pipeline.py"]
