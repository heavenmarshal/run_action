ARG BASE_IMAGE
FROM $BASE_IMAGE

ARG SOME_TOKEN
ENV SOME_TOKEN=${SOME_TOKEN}

RUN mkdir -p /etc/secrets && echo ${SOME_TOKEN} > /etc/secrets/some_token
RUN mkdir -p /app
WORKDIR /app
COPY integration.py /app
