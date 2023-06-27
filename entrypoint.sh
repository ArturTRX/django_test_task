#!/bin/sh
set -e

echo "Starting entrypoint.sh"

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

sleep 5

echo "Running Django migrations"

python manage.py makemigrations
python manage.py migrate

echo "Migrations completed"

echo "Starting import data script"

python manage.py import_data
echo "Data importing completed"

exec "$@"
