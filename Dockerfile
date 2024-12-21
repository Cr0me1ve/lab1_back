# Dockerfile for Backend
FROM python:3.11

WORKDIR /app

RUN pip install Flask

COPY . .

CMD ["python", "app.py"]
