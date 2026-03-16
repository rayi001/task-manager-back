#!/bin/bash
# Build React frontend
cd frontend && npm install && npm run build && cd ..

# Build Django backend
python manage.py migrate --noinput
python manage.py collectstatic --noinput
