# Stage 1: Build stage
FROM python:3.10 AS builder

# Install system dependencies required by mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    libmariadb-dev-compat \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies in a virtual environment
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2: Final stage
FROM python:3.10-slim

# Set environment variables for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

# Set the working directory in the container
WORKDIR /code

# Copy the virtual environment from the builder stage
COPY --from=builder /venv /venv

# Copy the current directory contents into the container at /code
COPY . /code/

# Expose port 8000
EXPOSE 8000

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
