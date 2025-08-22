FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV FLASK_BIND_ALL=true

COPY app.py .

CMD ["python", "app.py"]
