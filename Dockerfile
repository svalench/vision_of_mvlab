FROM python:3.9.1-slim-buster
# FROM python:3.9.1-alpine

LABEL mantainer='Mikalai Rysnik'

ENV PYTHONUNBUFFERED=1 \
    BASE_HOST=0.0.0.0 \
    BASE_PORT=50001 
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
# RUN python3 manage.py makemigrations
# RUN python manage.py migrate
COPY . /code/

EXPOSE ${BASE_PORT}

# CMD ["python3", "manage.py", "runserver", "$BASE_HOST:$BASE_PORT"]
# CMD "python3" "manage.py" "runserver" "${BASE_HOST}:${BASE_PORT}"
ENTRYPOINT "python3" "manage.py" "makemigrations &&" 
CMD "gunicorn" "--bind" "${BASE_HOST}:${BASE_PORT}" "project_v_0_0_1.wsgi"
