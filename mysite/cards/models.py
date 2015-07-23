from django.db import models
from django.contrib.auth.models import User
#Create your models here

class Card(models.Model):
   
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=60)
    url = models.URLField()
    image = models.ImageField()
    media_type = models.CharField(max_length=32)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name