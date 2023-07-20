FROM python:3.8
WORKDIR /app
RUN apt update && \
    apt install python3-pip -y

RUN python3 -m pip install --upgrade pip
COPY ./app /app
RUN pip3 install -r ./requirements.txt

