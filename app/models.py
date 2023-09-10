from typing import Dict,Tuple
from django.db import models
from uuid import uuid4
import os
from django.conf import settings
from tinymce.models import HTMLField
from . import utils
# Create your models here.

class ModelBase(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Banner(ModelBase):
    image = models.ImageField(upload_to='uploads/')

    def delete(self, using=None, keep_parents=False) -> Tuple[int, Dict[str, int]]:
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        return super().delete(using, keep_parents)


class Blog(ModelBase):
    title = models.CharField(max_length=200)
    short_desc = models.TextField(max_length=500)
    blog_body = HTMLField()
    slug = models.SlugField(null=True, blank=True, unique=True)
    created_on = models.DateField(auto_now=True)

    def save(self, *args, **kwargs) -> None:

        self.slug = utils.get_slug(self.title, Blog)
        return super(Blog, self).save(*args, **kwargs)

class Testimonial(ModelBase):
    image = models.ImageField(upload_to='uploads/')
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    desc = models.TextField()

    def delete(self, using=None, keep_parents=False) -> Tuple[int, Dict[str, int]]:
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        return super().delete(using, keep_parents)

class Program(ModelBase):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')
    desc = HTMLField()

    def delete(self, using=None, keep_parents=False) -> Tuple[int, Dict[str, int]]:
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        return super().delete(using, keep_parents)
