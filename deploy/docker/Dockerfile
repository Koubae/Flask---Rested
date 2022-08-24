# syntax=docker/dockerfile:1
FROM python:3.9-alpine3.16

ARG APP_DIR=/web/app
ARG APP_SRC=flask_rested/

WORKDIR ${APP_DIR}

# update alpine
#RUN apk add --update --no-cache \
#    curl \
#    build-base \
#    postgresql-dev

### install alpine packages
#RUN apk add --no-cache \
#  gcc \
#  musl-dev \
#  linux-headers

## Set up python env
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app/init.py
COPY ${APP_SRC}requirements.txt ${APP_DIR}
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ${APP_SRC} ${APP_DIR}

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["-m", "flask", "run", "--host=0.0.0.0"]