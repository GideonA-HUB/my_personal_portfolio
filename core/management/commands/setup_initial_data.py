from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import PersonalInfo, Skill, Project, Testimonial
from django.core.files.base import ContentFile
import os


class Command(BaseCommand):
    help = 'Set up initial data for the portfolio'

    def handle(self, *args, **options):
        self.stdout.write('Setting up initial portfolio data...')

        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Superuser created: admin/admin123'))

        # Create personal info if it doesn't exist
        if not PersonalInfo.objects.exists():
            personal_info = PersonalInfo.objects.create(
                name='Your Name',
                title='Full Stack Developer',
                bio='I am a passionate developer with experience in web development and software engineering.',
                email='your.email@example.com',
                phone='+1234567890',
                location='Your City, Country',
                availability='Mon - Fri: 9AM - 6PM',
                github='https://github.com/yourusername',
                linkedin='https://linkedin.com/in/yourusername',
            )
            self.stdout.write(self.style.SUCCESS('Personal info created'))

        # Create sample skills
        skills_data = [
            {'name': 'Python', 'percentage': 90, 'category': 'programming'},
            {'name': 'JavaScript', 'percentage': 85, 'category': 'programming'},
            {'name': 'Django', 'percentage': 88, 'category': 'framework'},
            {'name': 'React', 'percentage': 80, 'category': 'framework'},
            {'name': 'PostgreSQL', 'percentage': 75, 'category': 'database'},
            {'name': 'Git', 'percentage': 85, 'category': 'tool'},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Skill created: {skill.name}')

        # Create sample projects
        projects_data = [
            {
                'title': 'Portfolio Website',
                'description': 'A personal portfolio website built with Django and modern web technologies.',
                'github_url': 'https://github.com/yourusername/portfolio',
                'live_url': 'https://your-portfolio.com',
                'featured': True,
            },
            {
                'title': 'E-commerce Platform',
                'description': 'A full-featured e-commerce platform with payment integration.',
                'github_url': 'https://github.com/yourusername/ecommerce',
                'live_url': 'https://your-ecommerce.com',
                'featured': True,
            },
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Project created: {project.title}')

        # Create sample testimonials
        testimonials_data = [
            {
                'name': 'John Doe',
                'role': 'Client',
                'text': 'Excellent work and great communication throughout the project.',
                'show_on_homepage': True,
            },
            {
                'name': 'Jane Smith',
                'role': 'Colleague',
                'text': 'A reliable and skilled developer who always delivers quality work.',
                'show_on_homepage': True,
            },
        ]

        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                name=testimonial_data['name'],
                defaults=testimonial_data
            )
            if created:
                self.stdout.write(f'Testimonial created: {testimonial.name}')

        self.stdout.write(self.style.SUCCESS('Initial data setup completed successfully!')) 