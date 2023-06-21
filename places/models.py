from django.db import models


def image(instance,filename):
    imgename , extension = filename.split(".", 1)
    return "image_places/%s.%s"%(instance.id, extension)

class Place(models.Model):
    name = models.CharField(max_length=255)
    serves = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image, null=True)

    def __str__(self):
        return self.name

