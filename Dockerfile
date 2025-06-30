# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

RUN useradd --create-home ttuser
USER ttuser

# Expose port that Flask runs on
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
