from django.db import models


class Cluster(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1000)
    nodes = models.IntegerField()
