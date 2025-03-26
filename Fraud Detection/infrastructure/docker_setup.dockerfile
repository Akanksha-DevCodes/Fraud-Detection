# Use a base Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the dependencies file and install them
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . /app/

# Set the default command to run when the container starts
CMD ["python", "data_pipeline/kafka_producer.py"]