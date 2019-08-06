FROM python:3.7
ENV PORT 8080
EXPOSE 8080
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["app.py"]

# FROM golang:1.12.6-alpine3.9 as builder
# COPY main.go .
# RUN go build -o /app main.go

# FROM alpine:3.9
# CMD ["./app"]
# COPY --from=builder /app .
