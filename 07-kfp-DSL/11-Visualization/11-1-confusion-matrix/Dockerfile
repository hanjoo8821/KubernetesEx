FROM python:latest

RUN pip install sklearn pandas

COPY ./src /app
WORKDIR /app

CMD ["python", "/app/confusion_matrix.py"]