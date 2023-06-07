from django.db import models


class Teacher(models.Model):
    name = models.CharField("Name", max_length=240)

    def __str__(self):
        return self.name
