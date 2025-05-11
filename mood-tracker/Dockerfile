# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install system dependencies and required Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod +x /app/entrypoint.sh

# Expose port 8000 for Django
EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
