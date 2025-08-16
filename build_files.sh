#!/bin/bash
# Build script for Railway deployment

echo "Starting build process..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Check if DATABASE_URL is set
if [ -z "$DATABASE_URL" ]; then
    echo "Warning: DATABASE_URL not set. Using SQLite database."
fi

# Run database migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Set up initial data
echo "Setting up initial data..."
python manage.py setup_initial_data

echo "Build completed successfully!" 