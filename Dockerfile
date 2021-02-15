FROM python:3.9.1-slim-buster

LABEL mantainer='Mikalai Rysnik'

ENV PYTHONUNBUFFERED=1 \
    BASE_HOST=0.0.0.0 \
    BASE_PORT=50001 \
    DB_ENGINE=django.db.backends.postgresql_psycopg2 \
    DB_NAME=db1\
    DB_USER=mvlab\
    DB_PASSWORD=z1x2c3\
    DB_HOST=172.17.0.1\
    DB_PORT=5432\
    SUPERUSER_NAME=mvalb\
    SUPERUSER_EMAIL=info@mvlab.by\
    SUPERUSER_PASSWORD=z1x2c3\
    SOCKET_PORT=8086\
    DEBUG=True

WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/

EXPOSE ${BASE_PORT}

ENTRYPOINT  "python3" "manage.py" "makemigrations";\
            "python3" "manage.py" "migrate";\
            "gunicorn" "--bind" "${BASE_HOST}:${BASE_PORT}" "project_v_0_0_1.wsgi"