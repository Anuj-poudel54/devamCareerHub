from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('logout', views.logout_user, name='logout'),
    path('del/<str:id>/', views.delete_banner_image, name='delete-banner-image'),
    path('write', views.new_blog, name='add-blog'),
    path('blogs', views.blogs, name='blogs'),
    path('prev/<slug:slug>/', views.blog_preview, name='blog-preview'),
    path('edit/<slug:slug>/', views.edit, name='edit'),
    path('del-blog/<slug:slug>/', views.delete, name='delete-blog'),
    path('login/', views.login_user, name='login'),
    path('add-testmn/', views.add_testmn, name='add-testmn'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns.append(re_path('/*/', views.handle_404, name='404'))
