# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set a working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the Inventory Management System script
CMD ["python", "main.py"]
