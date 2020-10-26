FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt . 

RUN pip install Flask

COPY . .

EXPOSE 5001

CMD ["python", "temperature_server.py"]