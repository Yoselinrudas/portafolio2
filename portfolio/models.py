from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.

class Project(models.Model):
    image = ImageField(upload_to='portfolio/images/')
    title_proj = CharField(max_length = 50)
    Description = CharField(max_length = 80)
    tags = CharField(max_length = 50)
    url_git = URLField(blank=True)
