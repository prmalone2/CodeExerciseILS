from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

class Contact(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=9)
    emailAddress = models.CharField(max_length=200)
    streetAddress = models.CharField(max_length=200)

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)