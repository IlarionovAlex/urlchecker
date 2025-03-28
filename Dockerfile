# Use Python 3.9 as base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Python script
COPY app.py .

# Expose port 8000 for Prometheus metrics
EXPOSE 8000

# Run the app.py when the container starts
CMD ["python", "app.py"]