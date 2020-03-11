# Use of latest Python Version
FROM python:latest

# Define Python Buffer
ENV PYTHONUNBUFFERED 1

# Upgrade Pip
RUN pip install --upgrade pip

# Add Requirements file
ADD ./requirements.txt /app/requirements.txt

# Change workdir to App folder
WORKDIR /app

# Install Dependencies
RUN pip install -r requirements.txt

# Add App source file
ADD ./beer404 /app/beer404

# Change workdir for app launch
WORKDIR /app/beer404

# Open port for web app
EXPOSE 8010

# Launch command for server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]
