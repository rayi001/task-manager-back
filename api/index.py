import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

# Get the WSGI application
application = get_wsgi_application()

# Vercel serverless function handler
def handler(event, context):
    # This is a simplified handler for Vercel
    return application
