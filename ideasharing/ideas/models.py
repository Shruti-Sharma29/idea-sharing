from django.db import models

# Create your models here.

class shareidea(models.Model):
    username = models.CharField(max_length=150)
    full_name = models.CharField(max_length=150)
    email_address = models.EmailField(max_length=254)
    idea = models.CharField(max_length=254)
    descri_ption = models.TextField()

