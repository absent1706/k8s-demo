FROM python:3.7
EXPOSE 8080
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080"]
# CMD ["python", "app.py"]