from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import PersonalInfo, Skill, Project, Experience, Education, Testimonial


class Command(BaseCommand):
    help = 'Set up initial data for the portfolio'

    def handle(self, *args, **options):
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123456'
            )
            self.stdout.write(
                self.style.SUCCESS('Superuser created successfully!')
            )
            self.stdout.write('Username: admin')
            self.stdout.write('Password: admin123456')
        else:
            self.stdout.write('Superuser already exists.')

        # Create sample personal info if it doesn't exist
        if not PersonalInfo.objects.exists():
            PersonalInfo.objects.create(
                name='Gideon Amienghemhen',
                title='Full Stack Developer',
                bio='I\'m a passionate developer who loves creating beautiful and functional web applications. I specialize in modern web technologies and always strive to write clean, maintainable code.',
                email='gideon@example.com',
                phone='+1234567890',
                location='Your Location',
                availability='Mon - Fri: 9AM - 6PM PST',
                github='https://github.com/GideonA-HUB',
                linkedin='https://linkedin.com/in/gideon-amienghemhen',
                twitter='https://twitter.com/gideon_dev',
                instagram='https://instagram.com/gideon_dev'
            )
            self.stdout.write(
                self.style.SUCCESS('Sample personal info created!')
            )

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
                self.stdout.write(f'Created skill: {skill.name}')

        # Create sample project
        if not Project.objects.exists():
            project = Project.objects.create(
                title='Personal Portfolio Website',
                description='A modern, responsive portfolio website built with Django and Bootstrap. Features include dynamic content management, dark mode toggle, and mobile-responsive design.',
                github_url='https://github.com/GideonA-HUB/my_personal_portfolio',
                live_url='https://gideon-amienghemhen-portfolio.onrender.com',
                featured=True
            )
            # Add skills to project
            python_skill = Skill.objects.get(name='Python')
            django_skill = Skill.objects.get(name='Django')
            project.technologies.add(python_skill, django_skill)
            self.stdout.write('Sample project created!')

        # Create sample experience
        if not Experience.objects.exists():
            Experience.objects.create(
                title='Full Stack Developer',
                company='Your Company',
                location='Your City, Country',
                start_date='2023-01-01',
                current=True,
                description='Developed and maintained web applications using modern technologies. Collaborated with cross-functional teams to deliver high-quality software solutions.',
                technologies='Python, Django, JavaScript, React, PostgreSQL',
                order=1
            )
            self.stdout.write('Sample experience created!')

        # Create sample education
        if not Education.objects.exists():
            Education.objects.create(
                degree='Bachelor of Science in Computer Science',
                institution='Your University',
                location='Your City, Country',
                start_date='2019-09-01',
                end_date='2023-05-01',
                description='Studied computer science with focus on software engineering and web development.',
                gpa=3.8,
                relevant_courses='Data Structures, Algorithms, Web Development, Database Systems',
                order=1
            )
            self.stdout.write('Sample education created!')

        # Create sample testimonial
        if not Testimonial.objects.exists():
            Testimonial.objects.create(
                name='Ugo Joseph',
                role='Senior Developer',
                text='I had the pleasure of working with Gideon on several projects. His attention to detail and problem-solving skills are exceptional. He consistently delivers high-quality code and is always willing to help team members.',
                order=1,
                show_on_homepage=True
            )
            self.stdout.write('Sample testimonial created!')

        self.stdout.write(
            self.style.SUCCESS('Initial data setup completed successfully!')
        )
        self.stdout.write('You can now log in to /admin with:')
        self.stdout.write('Username: admin')
        self.stdout.write('Password: admin123456')
        self.stdout.write('IMPORTANT: Change the password after first login!') 