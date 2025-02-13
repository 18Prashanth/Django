from django.db import models

# Create your models here.


class ROom(models.Model):
    # host =
    # topic =
    name = models.CharField(max_length=200)
