from .models import Banner, Blog, Testimonial, Program
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

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title', 'image', 'desc']
