from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Contact, PersonalInfo, Experience, Education, Testimonial
from .forms import ContactForm


def home(request):
    """Home page view with personal info, skills, and featured projects"""
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    skills = Skill.objects.all()
    featured_projects = Project.objects.filter(featured=True)[:3]
    all_projects = Project.objects.all()[:6]
    testimonials = Testimonial.objects.filter(show_on_homepage=True)[:5]
    
    # Debug: Print profile image info
    if personal_info and personal_info.profile_image:
        print(f"Profile image exists: {personal_info.profile_image}")
        print(f"Profile image URL: {personal_info.profile_image.url}")
        print(f"Profile image path: {personal_info.profile_image.path}")
    
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'featured_projects': featured_projects,
        'all_projects': all_projects,
        'testimonials': testimonials,
    }
    return render(request, 'core/home.html', context)


def projects(request):
    """Projects page view"""
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'core/projects.html', context)


def project_detail(request, pk):
    """Individual project detail view"""
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        messages.error(request, 'Project not found.')
        return redirect('projects')
    
    context = {
        'project': project,
    }
    return render(request, 'core/project_detail.html', context)


def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send email notification (optional)
            try:
                send_mail(
                    f'New Contact Message: {contact.subject}',
                    f'From: {contact.name} ({contact.email})\n\nMessage:\n{contact.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except:
                pass  # Email sending failed, but contact is still saved
            
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    # Get personal info for contact details
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    context = {
        'form': form,
        'personal_info': personal_info,
    }
    return render(request, 'core/contact.html', context)


def about(request):
    """About page view"""
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    skills = Skill.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    testimonials = Testimonial.objects.all()
    
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'experience': experience,
        'education': education,
        'testimonials': testimonials,
    }
    return render(request, 'core/about.html', context) 