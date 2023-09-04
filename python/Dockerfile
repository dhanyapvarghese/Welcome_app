FROM python:3.8-alpine
RUN mkdir /app
ADD python/app.py /app
WORKDIR /app
RUN pip install flask
CMD ["python", "app.py"]
