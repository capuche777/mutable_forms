from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    changed_value = models.CharField(max_length=25, default='default value')

    def __str__(self):
        return self.name
