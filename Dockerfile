FROM alpine

ENV PROJECT_NAME=any_tools

RUN mkdir -p /app
RUN mkdir -p /app/staticfiles
WORKDIR /app

RUN apk update && apk add --no-cache --no-cache libffi-dev libc6-compat py-pip bash python3-dev gcc musl-dev supervisor \
    postgresql-dev nginx redis

ADD requirements/base.txt requirements/base.txt
ADD requirements/prod.txt requirements/prod.txt
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements/prod.txt

ADD . /app/

RUN python3 manage.py collectstatic --no-input
RUN python3 manage.py makemigrations

RUN chmod +x entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]
CMD ["serve"]
