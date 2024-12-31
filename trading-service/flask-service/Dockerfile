FROM python:3.9-slim

# Install git
RUN apt-get update && apt-get install -y git

WORKDIR /app

# Copy the entire flask-service folder to the /app/flask-service folder
COPY ./flask-service /app/flask-service

# Copy the alpaca-service folder from trading-service/ to /app/alpaca-service inside the container
COPY ./alpaca-service /app/alpaca_service

# Install Python dependencies from flask-service requirements.txt
COPY flask-service/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Install dependencies for alpaca-service
COPY alpaca-service/requirements.txt /app/alpaca-service/requirements.txt
RUN pip install -r /app/alpaca-service/requirements.txt

# Install Alpaca service package
RUN pip install /app/alpaca_service

EXPOSE 5000

CMD ["python", "/app/flask-service/run.py"]
