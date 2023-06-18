FROM python:3.11.4-alpine

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/

WORKDIR /app
