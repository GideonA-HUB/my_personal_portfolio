from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import PersonalInfo, Skill, Project, Contact


class Command(BaseCommand):
    help = 'Set up sample data for the portfolio website'

    def handle(self, *args, **options):
        self.stdout.write('Setting up sample data...')

        # Create personal info
        personal_info, created = PersonalInfo.objects.get_or_create(
            name="John Doe",
            defaults={
                'title': "Full Stack Developer",
                'bio': "I'm a passionate full-stack developer with 5+ years of experience in creating modern web applications. I specialize in Python, Django, React, and cloud technologies. I love solving complex problems and building user-friendly applications that make a difference.",
                'email': "john.doe@example.com",
                'phone': "+1 (555) 123-4567",
                'location': "San Francisco, CA",
                'github': "https://github.com/johndoe",
                'linkedin': "https://linkedin.com/in/johndoe",
                'twitter': "https://twitter.com/johndoe",
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created personal info'))
        else:
            self.stdout.write(self.style.WARNING('Personal info already exists'))

        # Create skills
        skills_data = [
            # Programming Languages
            {'name': 'Python', 'percentage': 95, 'category': 'programming'},
            {'name': 'JavaScript', 'percentage': 90, 'category': 'programming'},
            {'name': 'HTML/CSS', 'percentage': 95, 'category': 'programming'},
            {'name': 'Java', 'percentage': 80, 'category': 'programming'},
            {'name': 'C++', 'percentage': 75, 'category': 'programming'},
            
            # Frameworks
            {'name': 'Django', 'percentage': 90, 'category': 'framework'},
            {'name': 'React', 'percentage': 85, 'category': 'framework'},
            {'name': 'Vue.js', 'percentage': 80, 'category': 'framework'},
            {'name': 'Bootstrap', 'percentage': 90, 'category': 'framework'},
            {'name': 'Node.js', 'percentage': 75, 'category': 'framework'},
            
            # Databases
            {'name': 'PostgreSQL', 'percentage': 85, 'category': 'database'},
            {'name': 'MySQL', 'percentage': 80, 'category': 'database'},
            {'name': 'MongoDB', 'percentage': 70, 'category': 'database'},
            {'name': 'Redis', 'percentage': 75, 'category': 'database'},
            
            # Tools
            {'name': 'Git', 'percentage': 90, 'category': 'tool'},
            {'name': 'Docker', 'percentage': 80, 'category': 'tool'},
            {'name': 'AWS', 'percentage': 75, 'category': 'tool'},
            {'name': 'Linux', 'percentage': 85, 'category': 'tool'},
            {'name': 'VS Code', 'percentage': 95, 'category': 'tool'},
        ]

        created_skills = 0
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                created_skills += 1

        self.stdout.write(self.style.SUCCESS(f'✓ Created {created_skills} skills'))

        # Create projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured e-commerce platform built with Django and React. Features include user authentication, product management, shopping cart, payment integration, and admin dashboard.',
                'github_url': 'https://github.com/johndoe/ecommerce-platform',
                'live_url': 'https://ecommerce-demo.example.com',
                'featured': True,
            },
            {
                'title': 'Task Management App',
                'description': 'A collaborative task management application with real-time updates, team collaboration, and project tracking features. Built with Django REST API and Vue.js frontend.',
                'github_url': 'https://github.com/johndoe/task-manager',
                'live_url': 'https://taskmanager.example.com',
                'featured': True,
            },
            {
                'title': 'Portfolio Website',
                'description': 'A modern, responsive portfolio website built with Django and Bootstrap. Features include project showcase, skills display, contact form, and admin content management.',
                'github_url': 'https://github.com/johndoe/portfolio',
                'live_url': 'https://johndoe.dev',
                'featured': True,
            },
            {
                'title': 'Weather Dashboard',
                'description': 'A weather dashboard application that displays current weather and forecasts using multiple weather APIs. Built with Python Flask and Chart.js for data visualization.',
                'github_url': 'https://github.com/johndoe/weather-dashboard',
                'live_url': 'https://weather.example.com',
                'featured': False,
            },
            {
                'title': 'Blog Platform',
                'description': 'A content management system for blogs with features like rich text editing, categories, tags, comments, and SEO optimization. Built with Django and Bootstrap.',
                'github_url': 'https://github.com/johndoe/blog-platform',
                'live_url': 'https://blog.example.com',
                'featured': False,
            },
            {
                'title': 'Social Media Analytics',
                'description': 'A social media analytics dashboard that tracks engagement, follower growth, and content performance across multiple platforms. Built with Python and React.',
                'github_url': 'https://github.com/johndoe/social-analytics',
                'live_url': 'https://analytics.example.com',
                'featured': False,
            },
        ]

        created_projects = 0
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                created_projects += 1
                # Add some skills to projects
                if 'Django' in project_data['title'] or 'Portfolio' in project_data['title']:
                    django_skill = Skill.objects.filter(name='Django').first()
                    if django_skill:
                        project.technologies.add(django_skill)
                
                if 'React' in project_data['description']:
                    react_skill = Skill.objects.filter(name='React').first()
                    if react_skill:
                        project.technologies.add(react_skill)

        self.stdout.write(self.style.SUCCESS(f'✓ Created {created_projects} projects'))

        # Create sample contact messages
        contact_messages = [
            {
                'name': 'Alice Johnson',
                'email': 'alice@example.com',
                'subject': 'Project Collaboration',
                'message': 'Hi John, I saw your portfolio and I\'m impressed with your work. I have a project that I think would be a great fit for your skills. Would you be interested in discussing it?',
            },
            {
                'name': 'Bob Smith',
                'email': 'bob@techcompany.com',
                'subject': 'Job Opportunity',
                'message': 'Hello John, I\'m a hiring manager at TechCorp and I came across your portfolio. We\'re looking for a senior developer and your experience looks perfect. Are you open to new opportunities?',
            },
        ]

        created_contacts = 0
        for contact_data in contact_messages:
            contact, created = Contact.objects.get_or_create(
                email=contact_data['email'],
                subject=contact_data['subject'],
                defaults=contact_data
            )
            if created:
                created_contacts += 1

        self.stdout.write(self.style.SUCCESS(f'✓ Created {created_contacts} contact messages'))

        self.stdout.write(self.style.SUCCESS('\n🎉 Sample data setup completed successfully!'))
        self.stdout.write('\nYou can now:')
        self.stdout.write('1. Visit http://127.0.0.1:8000/ to see your portfolio')
        self.stdout.write('2. Go to http://127.0.0.1:8000/admin/ to manage content')
        self.stdout.write('3. Customize the sample data to match your information') 