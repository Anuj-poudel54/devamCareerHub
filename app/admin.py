from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['uid','image', 'created_on']

@admin.register(Blog)
class BlogAdming(admin.ModelAdmin):
    list_display = ['uid','title', 'short_desc', 'blog_body', 'slug', 'created_on']
