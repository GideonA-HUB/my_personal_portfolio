from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)
    category = models.CharField(max_length=50, choices=[
        ('programming', 'Programming'),
        ('framework', 'Framework'),
        ('database', 'Database'),
        ('tool', 'Tool'),
        ('other', 'Other'),
    ])
    icon = models.CharField(max_length=50, blank=True)
    
    class Meta:
        ordering = ['-percentage']
    
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500, blank=True, null=True, help_text="Image URL or path")
    technologies = models.ManyToManyField(Skill, blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.CharField(max_length=500, blank=True, null=True, help_text="Profile image URL or path")
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    availability = models.CharField(max_length=200, blank=True, help_text="e.g., Mon - Fri: 9AM - 6PM PST")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    
    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    technologies = models.CharField(max_length=500, blank=True, help_text="Comma-separated list of technologies used")
    order = models.IntegerField(default=0, help_text="Order in which to display (lower numbers first)")
    
    class Meta:
        ordering = ['-start_date', 'order']
    
    def __str__(self):
        if self.current:
            return f"{self.title} at {self.company} (Current)"
        return f"{self.title} at {self.company}"
    
    def get_duration(self):
        if self.current:
            return f"{self.start_date.strftime('%b %Y')} - Present"
        elif self.end_date:
            return f"{self.start_date.strftime('%b %Y')} - {self.end_date.strftime('%b %Y')}"
        return self.start_date.strftime('%b %Y')


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    relevant_courses = models.TextField(blank=True, help_text="Comma-separated list of relevant courses")
    order = models.IntegerField(default=0, help_text="Order in which to display (lower numbers first)")
    
    class Meta:
        ordering = ['-start_date', 'order']
    
    def __str__(self):
        if self.current:
            return f"{self.degree} at {self.institution} (Current)"
        return f"{self.degree} at {self.institution}"
    
    def get_duration(self):
        if self.current:
            return f"{self.start_date.strftime('%b %Y')} - Present"
        elif self.end_date:
            return f"{self.start_date.strftime('%b %Y')} - {self.end_date.strftime('%b %Y')}"
        return self.start_date.strftime('%b %Y')


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, help_text="e.g., Client, Colleague, Mentor")
    text = models.TextField()
    photo = models.CharField(max_length=500, blank=True, null=True, help_text="Photo URL or path")
    order = models.IntegerField(default=0, help_text="Order in which to display (lower numbers first)")
    show_on_homepage = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Review & Recommendation"
        verbose_name_plural = "Reviews & Recommendations"

    def __str__(self):
        return f"{self.name} ({self.role})" if self.role else self.name 