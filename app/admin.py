from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['uid','image', 'created_on']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['uid','title', 'short_desc', 'blog_body', 'slug', 'created_on']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['uid','name', 'location', 'desc', 'image', 'created_on']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['uid','title', 'desc', 'image', 'created_on']
