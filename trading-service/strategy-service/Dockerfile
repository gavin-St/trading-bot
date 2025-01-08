FROM python:3.9-slim

# Install git
RUN apt-get update && apt-get install -y git

WORKDIR /app

COPY ./strategy-service /app/strategy-service

COPY ./alpaca-service /app/alpaca_service

COPY strategy-service/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Install dependencies for alpaca-service
COPY alpaca-service/requirements.txt /app/alpaca-service/requirements.txt
RUN pip install -r /app/alpaca-service/requirements.txt

# Install Alpaca service package
RUN pip install /app/alpaca_service

EXPOSE 5000

CMD ["python", "/app/strategy-service/scheduler/scheduler.py"]
