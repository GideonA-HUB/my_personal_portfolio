# Modern Portfolio Website

A beautiful, responsive portfolio website built with Django, featuring modern design, smooth animations, and a comprehensive content management system.

## 🚀 Features

- **Modern Design**: Clean, responsive design with beautiful animations
- **Content Management**: Easy-to-use Django admin for managing portfolio content
- **Project Showcase**: Display your projects with images, descriptions, and links
- **Skills Section**: Showcase your technical skills with progress bars
- **Contact Form**: Functional contact form with email notifications
- **Responsive**: Mobile-first design that works on all devices
- **SEO Friendly**: Optimized for search engines
- **Fast Loading**: Optimized static files and efficient database queries

## 🛠️ Technologies Used

- **Backend**: Python 3.8+, Django 4.2
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Bootstrap 5, Custom CSS
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Poppins)
- **Database**: SQLite (development), PostgreSQL (production ready)

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd my_portforlio
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Set up sample data (optional)**
   ```bash
   python manage.py setup_sample_data
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the website**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
my_portforlio/
├── portfolio/                 # Main Django project
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── core/                     # Main app
│   ├── __init__.py
│   ├── admin.py              # Django admin configuration
│   ├── apps.py               # App configuration
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── urls.py               # App URL patterns
│   └── forms.py              # Django forms
├── templates/                # HTML templates
│   ├── base.html             # Base template
│   └── core/                 # App-specific templates
│       ├── home.html
│       ├── about.html
│       ├── projects.html
│       ├── project_detail.html
│       └── contact.html
├── static/                   # Static files
│   ├── css/
│   │   └── style.css         # Custom styles
│   └── js/
│       └── main.js           # Custom JavaScript
├── media/                    # User-uploaded files
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🎨 Customization

### Personal Information
1. Go to Django admin: http://127.0.0.1:8000/admin/
2. Navigate to "Core" → "Personal infos"
3. Add or edit your personal information

### Projects
1. In Django admin, go to "Core" → "Projects"
2. Add your projects with:
   - Title and description
   - Project image (optional)
   - GitHub and live URLs
   - Associated technologies

### Skills
1. In Django admin, go to "Core" → "Skills"
2. Add your skills with:
   - Skill name
   - Proficiency percentage (0-100)
   - Category (Programming, Framework, Database, Tool, Other)

### Styling
- Edit `static/css/style.css` to customize colors, fonts, and layout
- Modify `templates/base.html` for structural changes
- Update `static/js/main.js` for JavaScript functionality

## 🌐 Deployment

### Production Settings
1. Update `settings.py`:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   SECRET_KEY = 'your-secret-key-here'
   ```

2. Set up environment variables:
   ```bash
   export DJANGO_SETTINGS_MODULE=portfolio.settings
   export SECRET_KEY='your-secret-key'
   ```

3. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

4. Set up a production database (PostgreSQL recommended)

### Deployment Options
- **Heroku**: Easy deployment with Git integration
- **DigitalOcean**: VPS with full control
- **AWS**: Scalable cloud infrastructure
- **Vercel**: Fast static hosting (with API routes)

## 📱 Features Overview

### Home Page
- Hero section with personal introduction
- Skills showcase with animated progress bars
- Featured projects display
- Call-to-action section

### About Page
- Detailed personal information
- Skills breakdown by category
- Experience timeline
- Downloadable resume

### Projects Page
- Grid layout of all projects
- Search and filter functionality
- Project categories
- Technology tags

### Contact Page
- Functional contact form
- Contact information display
- Social media links
- FAQ section

## 🔧 Management Commands

### Setup Sample Data
```bash
python manage.py setup_sample_data
```
This command creates sample projects, skills, and personal information for demonstration.

### Clear Sample Data
```bash
python manage.py clear_sample_data
```
This command removes all sample data from the database.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Bootstrap for the responsive framework
- Font Awesome for the beautiful icons
- Google Fonts for the typography
- Django community for the excellent framework

## 📞 Support

If you have any questions or need help with the portfolio website, please:

1. Check the [Issues](https://github.com/yourusername/my_portforlio/issues) page
2. Create a new issue with a detailed description
3. Contact me directly at your-email@example.com

---

**Happy coding! 🚀** 