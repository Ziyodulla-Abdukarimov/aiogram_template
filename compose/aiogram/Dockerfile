# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV TZ=UTC

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    tzdata \
    && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY /requirements/requirements.txt /app/requirements/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements/requirements.txt

# Copy the rest of your application code into the container
COPY . /app/

# Expose any necessary ports
# EXPOSE 80

# Define the command to run your application
CMD ["python", "app.py"]
