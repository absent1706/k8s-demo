FROM python:3.7
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN adduser --disabled-password --gecos "" non-root-user
USER non-root-user
CMD ["celery", "-A", "worker", "worker", "--loglevel=INFO"]
