FROM python:3.7
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

#CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080"]
CMD ["celery", "-A", "worker", "worker", "--loglevel=INFO", "--concurrency=10"]
