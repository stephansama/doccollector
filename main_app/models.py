from django.db import models
from django.urls import reverse

# Create your models here.


class Document(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"doc_id": self.id})
