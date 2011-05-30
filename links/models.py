from django.db import models

class Link (models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=140)