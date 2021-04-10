from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=122)
    query = models.TextField()
    date = models.DateField()
class Chat(models.Model):
    email1 = models.CharField(max_length=122,null=True,blank=True)
    email2 = models.CharField(max_length=122,null=True,blank=True)
    email3 = models.CharField(max_length=122,null=True,blank=True)
    email4 = models.CharField(max_length=122,null=True,blank=True)
class Chat1(models.Model):
    email = models.CharField(max_length=122,null=True,blank=True)
    
