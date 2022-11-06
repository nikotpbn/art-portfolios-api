FROM python:alpine3.16

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./scripts /scripts
COPY ./backend /backend
WORKDIR /backend
EXPOSE 8000

# https://stackoverflow.com/questions/56048631/docker-alpine-error-loading-mysqdoldb-module
# https://pillow.readthedocs.io/en/latest/installation.html
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev py3-setuptools musl-dev && \
    apk add --no-cache mariadb-dev && \
    apk add tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev

RUN pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

RUN mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chmod -R +x /scripts

ENV PATH="/scripts:$PATH"
CMD [ "entrypoint.sh" ]