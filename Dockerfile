# Use the official Python image from Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the entire project directory into the container
COPY . /code/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

# Command to run the Python application
CMD ["pytest"]
