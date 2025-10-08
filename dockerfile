# STAGE 1: Builder - Installs dependencies
# We use a robust Python base image for installation, which includes tools 
# necessary to compile packages like psycopg2 (PostgreSQL adapter).
FROM python:3.11-slim as builder

# Set environment variable to prevent Python from buffering its output, 
# which makes logs appear immediately in the container runtime.
ENV PYTHONUNBUFFERED 1

# Install system dependencies required for building psycopg2 and other packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory for the dependencies
WORKDIR /app

# Copy the requirements file and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- STAGE 2: Final Runtime Image ---
# Use a smaller Python base image for the final runtime environment.
FROM python:3.11-slim

# Install only the runtime dependency for PostgreSQL client (libpq5)
# This is much smaller than installing all the development libraries.
RUN apt-get update && apt-get install -y --no-install-recommends libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Set the primary working directory inside the container
WORKDIR /usr/src/app

# Copy only the installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy all application code (manage.py, apps, project files)
# Assuming this Dockerfile is in the 'backend' folder.
COPY . /usr/src/app/

# Expose the port Gunicorn will listen on
EXPOSE 8000

# Command to run the application:
# 1. Collect static files (if needed for admin/static endpoints)
# 2. Run database migrations (ensures the database schema is up-to-date)
# 3. Start the Gunicorn WSGI server for production-grade serving
CMD ["/bin/bash", "-c", "python manage.py collectstatic --noinput && python manage.py migrate --noinput && gunicorn flint_project.wsgi:application --bind 0.0.0.0:8000"]
