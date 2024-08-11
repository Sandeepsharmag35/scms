# Stage 1: Build Stage
FROM python:3.10 AS builder

# Set environment variables for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Copy only the requirements file to install dependencies first
COPY requirements.txt /code/

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    libmariadb-dev-compat \
    && rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment
RUN python -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install --no-cache-dir -r /code/requirements.txt

# Stage 2: Final Stage
FROM python:3.10-slim

# Set environment variables for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Copy only the necessary files from the build stage
COPY --from=builder /venv /venv
COPY . /code/

# Set environment variable for Python path
ENV PATH="/venv/bin:$PATH"

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
