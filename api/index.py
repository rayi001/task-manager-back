import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

# Run migrations on first deployment (only in production)
if os.environ.get('VERCEL_ENV') == 'production':
    try:
        execute_from_command_line(['manage.py', 'migrate', '--noinput'])
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    except Exception as e:
        print(f"Migration/collection error: {e}")

# Get the WSGI application
application = get_wsgi_application()

# Vercel serverless function handler
def handler(event, context):
    return application
