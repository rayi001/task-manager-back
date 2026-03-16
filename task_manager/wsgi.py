"""
WSGI config for task_manager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

# Run migrations on startup for serverless environments
if os.environ.get('VERCEL') or os.environ.get('AWS_LAMBDA_FUNCTION_NAME'):
    try:
        execute_from_command_line(['manage.py', 'migrate', '--noinput'])
    except Exception as e:
        print(f"Migration error: {e}")

application = get_wsgi_application()
