# Use a base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 8000

# Start the application
CMD ["python","manage.py","migrate","python","manage.py","runserver","0.0.0.0:8000"]
