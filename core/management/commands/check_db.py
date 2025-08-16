from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'Check database connectivity and configuration'

    def handle(self, *args, **options):
        self.stdout.write('Checking database configuration...')
        
        # Check environment variables
        database_url = os.environ.get('DATABASE_URL', 'Not set')
        self.stdout.write(f'DATABASE_URL: {database_url[:50]}...' if len(database_url) > 50 else f'DATABASE_URL: {database_url}')
        
        # Check Django database settings
        db_settings = settings.DATABASES['default']
        self.stdout.write(f'Database Engine: {db_settings.get("ENGINE", "Not set")}')
        self.stdout.write(f'Database Name: {db_settings.get("NAME", "Not set")}')
        self.stdout.write(f'Database Host: {db_settings.get("HOST", "Not set")}')
        self.stdout.write(f'Database Port: {db_settings.get("PORT", "Not set")}')
        
        # Try to connect to database
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT version();")
                version = cursor.fetchone()
                self.stdout.write(self.style.SUCCESS(f'Database connection successful!'))
                self.stdout.write(f'Database version: {version[0]}')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Database connection failed: {e}'))
            
        # Check if migrations table exists
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = 'django_migrations'
                    );
                """)
                exists = cursor.fetchone()[0]
                if exists:
                    self.stdout.write(self.style.SUCCESS('Migrations table exists'))
                else:
                    self.stdout.write(self.style.WARNING('Migrations table does not exist'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Could not check migrations table: {e}'))
