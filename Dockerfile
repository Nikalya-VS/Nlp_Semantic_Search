FROM python:3.11-slim

# Prevent Python from creating .pyc files
# and ensure logs appear immediately
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project
COPY app ./app
COPY frontend ./frontend
COPY data ./data
COPY logs ./logs
COPY scripts ./scripts

# Default command
# Docker Compose will override this for each service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]