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