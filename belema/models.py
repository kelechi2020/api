from django.db import models

class Belema(models.Model):
    name = models.CharField(verbose_name="YOUR NAME", max_length=25)
    skin_colour = models.CharField(verbose_name="SKIN COLOUR", max_length=300)
    age = models.IntegerField()
    instituition = models.CharField(verbose_name="SCHOOL ATTENDED", max_length=30)

    def __str__(self):
        return self.name