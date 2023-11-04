FROM hub.hamdocker.ir/python:3.9

ENV PYTHONUNBUFFERED=1
ENV UPLOAD_FOLDER /uploads
RUN mkdir -p $UPLOAD_FOLDER

# Install any additional dependencies you need
RUN apt-get update
RUN apt-get install -y libxml2-dev libgl1-mesa-glx


COPY . /

WORKDIR /

RUN pip install -r requirements.txt

EXPOSE 6060

CMD python main.py

