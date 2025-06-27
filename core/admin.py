from django.contrib import admin
from .models import Skill, Project, Contact, PersonalInfo, Experience, Education, Testimonial


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'category']
    list_filter = ['category']
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description']
    filter_horizontal = ['technologies']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'read', 'created_at']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']
    search_fields = ['name', 'title', 'email']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'bio', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location', 'availability')
        }),
        ('Social Media', {
            'fields': ('github', 'linkedin', 'twitter', 'instagram')
        }),
        ('Documents', {
            'fields': ('resume',)
        }),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'current', 'order']
    list_filter = ['current', 'start_date', 'end_date']
    search_fields = ['title', 'company', 'description']
    list_editable = ['order']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company', 'location', 'order')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'current')
        }),
        ('Details', {
            'fields': ('description', 'technologies')
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'current', 'gpa', 'order']
    list_filter = ['current', 'start_date', 'end_date']
    search_fields = ['degree', 'institution', 'description']
    list_editable = ['order']
    fieldsets = (
        ('Basic Information', {
            'fields': ('degree', 'institution', 'location', 'order')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'current')
        }),
        ('Academic Details', {
            'fields': ('description', 'gpa', 'relevant_courses')
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'show_on_homepage', 'order', 'created_at']
    list_filter = ['show_on_homepage', 'created_at']
    search_fields = ['name', 'role', 'text']
    list_editable = ['order', 'show_on_homepage']
    fieldsets = (
        (None, {
            'fields': ('name', 'role', 'text', 'photo', 'order', 'show_on_homepage')
        }),
    ) 