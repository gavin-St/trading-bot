FROM python:3.9-slim

WORKDIR /app

# Copy Flask service files
COPY flask-service/ /app

# Copy Alpaca service package
COPY alpaca-service/ /app/alpaca-service

# Install dependencies
COPY flask-service/requirements.txt /app
RUN pip install -r requirements.txt

# Install Alpaca service package
RUN pip install /app/alpaca-service

EXPOSE 5000

CMD ["python", "run.py"]
