#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running database migrations..."
python manage.py migrate

echo "Creating default Admin Superuser..."
# This safely creates an admin account (username: admin, password: admin) if it doesn't already exist
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

echo "Fetching Apple Products into database..."
python manage.py sync_apple_products

echo "Build complete!"
