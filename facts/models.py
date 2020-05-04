from djongo import models

# Create your models here.

class Object(models.Model):
    name = models.CharField(max_length=4096)

    class Meta:
        abstract = True

class Person(Object):
    birthdate = models.DateField()

class Farm(Object):
    name = models.CharField(max_length=4096)
