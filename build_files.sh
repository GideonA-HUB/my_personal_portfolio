#!/usr/bin/env bash
# exit on error
set -o errexit

# Install system dependencies for PostgreSQL
apt-get update -qq && apt-get install -y postgresql-client

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate --noinput 