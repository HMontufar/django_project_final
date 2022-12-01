from django.db import models

class Hobbie(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} | email: {self.email}"