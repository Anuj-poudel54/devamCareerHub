from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-login'),
    path('', include('app.urls')),
    path('write/', include('tinymce.urls')),
]

