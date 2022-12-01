from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    email = models.EmailField()
    collection = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.modelo}"
