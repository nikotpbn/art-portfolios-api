FROM python:alpine3.16

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./backend /backend
WORKDIR /backend


RUN pip install -r /tmp/requirements.txt && \
    rm -rf /tmp