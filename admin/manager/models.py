from django.db import models

class Persion():

    name = models.CharField(max_length=32)
    birthday = models.DataTimeField()
    sex = models.IntegerField(editable=False)
    address_from = models.IntegerField()
    current_address = models.IntegerField()
    email = models.EmailField()

class Manager(models.Modle):

    person = models.ForeignKey('Person')
    department = models.IntegerField()
    joined_at = models.DateTimeField()
    quited_at = models.DataTimeField(null=True, blank=True)

class Worker(models.Model):

    person = models.ForeignKey('Person')
    department = models.IntegerField()
    joined_at = models.DateTimeField()
    quited_at = models.DataTimeField(null=True, blank=True)
    manager = models.ForeignKey('Manager')