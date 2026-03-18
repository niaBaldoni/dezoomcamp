FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install dbt-duckdb
RUN pip install --no-cache-dir \
    dbt-duckdb==1.8.0 \
    requests

# Create workspace directory
WORKDIR /workspace

# Set environment variables
ENV DBT_PROFILES_DIR=/workspace/.dbt

CMD ["/bin/bash"]
