from django.db import models

# Create your models here.


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title