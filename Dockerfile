FROM python:alpine3.16

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./scripts /scripts
COPY ./backend /backend
WORKDIR /backend
EXPOSE 8000

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add --no-cache mariadb-dev

RUN pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

RUN mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chmod -R +x /scripts

ENV PATH="/scripts:$PATH"
CMD [ "entrypoint.sh" ]