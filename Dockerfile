FROM hub.hamdocker.ir/ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y   
RUN apt-get install -y python3 python3-pip python3-dev
RUN apt-get install -y libxml2-dev
RUN apt-get install -y libgl1-mesa-glx 
COPY . /

WORKDIR /

RUN pip install -r requirements.txt

EXPOSE 6060

CMD ["python3", "main.py"]
