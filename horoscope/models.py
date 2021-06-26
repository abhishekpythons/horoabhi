from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    DOB = models.DateField()

    @classmethod
    def create(cls, name, DOB):
        person = cls(name=name, DOB=DOB)
        # do something with the book
        return person