FROM python:3.10-slim-buster

WORKDIR /chatbot

COPY . /chatbot

RUN pip install requirements.txt

CMD ["python3", app.py]