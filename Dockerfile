FROM python:3.9.1-slim-buster
LABEL mantainer='Mikalai Rysnik'

ENV PYTHONUNBUFFERED=1 \
    BASE_HOST=0.0.0.0 \
    BASE_PORT=50001 
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE ${BASE_PORT}

# CMD ["python3", "manage.py", "runserver", "$BASE_HOST:$BASE_PORT"]
CMD "python3" "manage.py" "runserver" "${BASE_HOST}:${BASE_PORT}"