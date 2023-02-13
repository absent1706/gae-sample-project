FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:8080 main:app
# CMD gunicorn --bind 0.0.0.0:8080 main:app --capture-output --log-level debug
#CMD python main.py
# [END dockerfile]
