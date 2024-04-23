# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /dashboard

# Install any needed packages specified in requirements.txt
COPY requirements.txt /dashboard/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of your application's code
COPY . /dashboard/

# Make port 8000 available outside this container
EXPOSE 8000

# Define the command to run your app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dashboard.wsgi.application"]
OD
