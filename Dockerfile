# Build stage
# Base Image
FROM python:3.13-alpine3.20 AS builder

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./

RUN apk update && apk add --no-cache gcc musl-dev libffi-dev && \
    python-3 -m venv /app/venv && \
    /app/venv/bin/pip install --no-cache-dir setuptools && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Production stage
FROM python:3.13-alpine3.20

# Set working directory
WORKDIR /app/api

# Copy necessary files from build stage
COPY --from=builder /app /app

# Create a non root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Change ownership of the application files to the non root user
RUN chown -R appuser:appgroup /app

# Switch to the non root user
USER appuser

# Expose the port the app runs on
EXPOSE 3000

# Set the PATH to include the virtual environment's bin directory
ENV PATH="/app/venv/bin:$PATH"

CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]
