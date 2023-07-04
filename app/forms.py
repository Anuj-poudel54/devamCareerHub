from typing import Any
from .models import Banner, Blog, Testimonial
from django import forms

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['image']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'short_desc', 'blog_body']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'image', 'location', 'desc']
