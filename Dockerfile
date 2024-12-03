# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py /app/
COPY requirements.txt /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn for production WSGI server
RUN pip install gunicorn

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Use Gunicorn to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
