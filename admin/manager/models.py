from django.db import models
#from django.contrib.auth.models import AbstractBaseUser
#from manager.managers import PersonManager


class Person(models.Model):
    #objects = PersionManager()

    name = models.CharField(max_length=32)
    birthday = models.DateTimeField()
    sex = models.IntegerField(editable=False)
    address_from = models.IntegerField()
    current_address = models.IntegerField()
    email = models.EmailField()


class Manager(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    department = models.IntegerField()
    joined_at = models.DateTimeField()
    quited_at = models.DateTimeField(null=True, blank=True)


class Worker(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    department = models.IntegerField()
    joined_at = models.DateTimeField()
    quited_at = models.DateTimeField(null=True, blank=True)
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE)
