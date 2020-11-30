from django.db import models

# Create your models here.

class ModelExample(models.Model):
    especie = models.CharField(max_length=64)
    edad = models.IntegerField()

    def __str__(self):
        return self.especie
