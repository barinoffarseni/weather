FROM python:3-alpine
WORKDIR /home/python/app
COPY ./requirements.txt /home/python/app
RUN pip install --no-cache-dir -r requirements.txt