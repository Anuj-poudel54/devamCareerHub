
from django.utils.text  import slugify
import uuid

def get_slug(title, model):

    slug = slugify(title)
    while model.objects.filter(slug=slug).exists():
        slug = f'{slugify(title)}-{str(uuid.uuid4())[:4]}'
    
    return slug