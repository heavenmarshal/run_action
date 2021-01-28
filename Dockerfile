FROM python:3.7
COPY app /app
WORKDIR /app
RUN mkdir -p /etc/python-app-config
COPY config/config.json /etc/python-app-config/
