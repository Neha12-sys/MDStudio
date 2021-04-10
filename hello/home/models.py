from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=122)
    query = models.TextField()
    date = models.DateField()