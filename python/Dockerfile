FROM python:3.8
RUN mkdir /app
ADD python/app.py /app
WORKDIR /app
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
