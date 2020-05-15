from djongo import models

# Create your models here.

class Object(models.Model):
    name = models.CharField(max_length=4096)
    type = models.CharField(max_length=4096)

    class Meta:
        abstract = True

class Person(Object):
    birthdate = models.DateField()

class Point2D(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    class Meta:
        abstract = True

class Polygon(models.Model):
    coordinates = models.ArrayField(model_container=Point2D)

    class Meta:
        abstract = True

class MultiPolygon(models.Model):
    polygons = models.ArrayField(model_container=Polygon)

    class Meta:
        abstract = True

class Organization(models.Model):
    name = models.CharField(max_length=4096)
    type = models.CharField(max_length=4096)
    additional_info = models.TextField()

class Company(Organization):
    owners = models.ArrayReferenceField(to=Person, on_delete=models.CASCADE, related_name='companies_owned')
    employees = models.ArrayReferenceField(to=Person, on_delete=models.CASCADE, related_name='companies_employed_by')

class Faciliity(models.Model):
    location = models.EmbeddedField(model_container=MultiPolygon)
    type = models.CharField(max_length=4096)
    description = models.TextField()

