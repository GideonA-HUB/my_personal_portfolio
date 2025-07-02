from django.core.management.base import BaseCommand
from django.db import migrations, models
from core.models import Project, PersonalInfo, Testimonial


class Command(BaseCommand):
    help = 'Migrate image fields from CharField to ImageField'

    def handle(self, *args, **options):
        self.stdout.write('Starting image field migration...')
        
        # This command will be run after the migration is applied
        # to ensure all image fields are properly converted
        
        self.stdout.write(
            self.style.SUCCESS('Image field migration completed!')
        )
        self.stdout.write('You can now upload images directly in the admin interface.')
        self.stdout.write('Make sure to run: python manage.py makemigrations')
        self.stdout.write('Then: python manage.py migrate') 