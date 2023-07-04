from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import BannerForm, BlogForm, TestimonialForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):

    if request.method == "POST":
        banner_form_with_data = BannerForm(request.POST, request.FILES)
        if banner_form_with_data.is_bound and banner_form_with_data.is_valid():
            banner_form_with_data.save()
            messages.success(request, "New banner added!")

    banner_images = models.Banner.objects.all().order_by('-created_on')
    banner_form = BannerForm()
    testimonial_form = TestimonialForm()
    testimonials = models.Testimonial.objects.all()
    context = {'banner_images': banner_images,
               'banner_form': banner_form,
                'testimonial_form': testimonial_form,
                'testimonials': testimonials}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'read.html')

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Loggedout successfully!")
    return redirect('/')

@login_required
def delete_banner_image(request, id):
    try:
        banner_image = models.Banner.objects.get(uid = id)
        banner_image.delete()
        messages.success(request, "Banner image deleted!")
    except models.Banner.DoesNotExist:
        messages.error(request, "This Banner does not exist!")
        
    return redirect('/')

@login_required
def new_blog(request):

    if request.method == "POST":
        blog_form_with_data = BlogForm(request.POST, request.FILES)
        print(blog_form_with_data.is_valid())
        if blog_form_with_data.is_valid():
            blog_form_with_data.save()
            messages.success(request, "New blog created!")


    blog_form = BlogForm()
    return render(request, 'writeBlog.html', {'blog_form': blog_form})


def blogs(request):

    blogs = models.Blog.objects.all()

    return render(request, 'blogs.html', {'blogs': blogs})

def blog_preview(request, slug):

    blog = models.Blog.objects.filter(slug=slug)
    if not blog.exists():
        messages.warning(request, "Blog does not exist!")
        return redirect('blogs')
    
    blog = blog.first()

    return render(request, 'blogPreview.html', {'blog': blog})


@login_required
def edit(request, slug):
    blog = models.Blog.objects.filter(slug=slug)
    if not blog.exists():
        messages.info("Blog does not exists.")
        return redirect('blogs')
    blog = blog.first()
    if request.method == "POST":
        updated_blog = BlogForm(request.POST, request.FILES, instance=blog)
        if updated_blog.is_valid():
            updated_blog.save()
            messages.success(request, "Blog updated!")

    blog_form = BlogForm(instance=blog)
    return render(request, 'editBlog.html', {'blog_form': blog_form})

@login_required
def delete(request, slug):
    blog = models.Blog.objects.filter(slug=slug)
    if not blog.exists():
        messages.info("Blog does not exists.")
        return redirect('blogs')
    
    blog.first().delete()
    messages.success(request, "Blog deleted!")
    return redirect('blogs')

def login_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(username=username, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('/')
        else:
            messages.warning(request,  "*Invalid credential")
            return redirect('login')

    return render(request, 'login.html')

def handle_404(request):
    return render(request, 'page404.html')

@login_required
def add_testmn(request):
    if request.method == "POST":
        testmn_data = TestimonialForm(request.POST, request.FILES)
        if testmn_data.is_valid():
            testmn_data.save()
            messages.success(request, "Testimonial added successfully!")

        else:
            messages.error(request, "Something went wrong!")
    return redirect('/')
