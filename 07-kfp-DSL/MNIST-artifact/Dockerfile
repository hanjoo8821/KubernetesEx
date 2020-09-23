FROM tensorflow/tensorflow:latest

RUN mkdir -p /app
ADD ml-mnist.py /app/
WORKDIR /app

CMD ["python", "/app/ml-mnist.py"]
