from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    salary = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.subject
