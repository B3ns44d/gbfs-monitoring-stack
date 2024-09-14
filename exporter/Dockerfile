# Stage 1: Builder Stage
FROM python:3.10-slim AS builder

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /build

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Stage 2: Production Stage
FROM python:3.10-slim

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user for security
RUN addgroup --system exporter && adduser --system --ingroup exporter exporter

# Set work directory
WORKDIR /src

# Copy installed Python packages from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code
COPY src/ /src/

# Copy configuration files
COPY configs/ /src/configs/

# Change ownership to the non-root user
RUN chown -R exporter:exporter /src

# Switch to the non-root user
USER exporter

# Expose the port on which the exporter will run
EXPOSE 8000

# Define the entry point
ENTRYPOINT ["python", "main.py"]

# Default arguments
CMD ["--config", "configs/providers.yaml", "--port", "8000"]
