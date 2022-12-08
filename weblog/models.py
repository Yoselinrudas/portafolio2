from django.db import models

import datetime
# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='weblog/images/')
    title_proj = models.CharField(max_length = 100)
    description = models.TextField()
    tags = models.CharField(max_length = 50)
    url_git = models.URLField(blank=True)
    date = models.DateField(datetime.date.today)