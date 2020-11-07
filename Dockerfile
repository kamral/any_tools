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

RUN echo "DEBUG=off" >> /app/project/settings/.env
RUN echo "DATABASE_URL=psql://onytrex_chat:xxWrbvp7GD6jEjzvwEXvuLKaT9PAFmCN@tugush.cloctommwngl.eu-central-1.rds.amazonaws.com:5432/wallet_db" >> /app/project/settings/.env
#RUN echo "BTC_WALLETPASS=asdqwe123" >> /app/project/settings/.env
RUN echo "SECRET_KEY=wl4xt0nbvgo0qe9e9s6jsrl!18jc3vg&elu=m5ott6gel(dv*2" >> /app/project/settings/.env
RUN echo "MAIL_ADDRESS=kamral010101@gmail.com" >> /app/project/settings/.env
RUN echo "MAIL_PASSWORD=kamral010101" >> /app/project/settings/.env

RUN pip3 install gunicorn

RUN mkdir -p /run/nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

COPY config/nginx.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /etc/supervisor.d
COPY config/supervisord.conf /etc/supervisord.conf

RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput

EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
