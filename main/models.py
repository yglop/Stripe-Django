from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0) #cents

    def __str__(self):
        return self.name

