from django.db import models

# Create your models here.

class blog(models.Model):
    topic=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to='photos/')
    desc=models.TextField()
