from django.db import models
from .utils.unique_id import generate_unique_id


class Image(models.Model):

    unique_id = models.CharField(max_length=50, default=generate_unique_id)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.unique_id} -- {self.title}"
