#!/usr/bin/env python
import os
import django
from django.core.management import execute_from_command_line

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

# Setup Django
django.setup()

# Run migrations
try:
    execute_from_command_line(['manage.py', 'migrate', '--noinput'])
    print("✅ Migrations completed successfully!")
except Exception as e:
    print(f"❌ Migration error: {e}")
    import traceback
    print(traceback.format_exc())
