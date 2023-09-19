from django.db import models


# Create your models here.
class Extracurricular(models.Model):
    # Basic Fields
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)

    # Integer Fields
    field = models.IntegerField(null=True)
    type = models.IntegerField(null=True)
    mode = models.IntegerField(null=True)
    season = models.IntegerField(null=True)
    selectivity = models.IntegerField(null=True)
    cost = models.IntegerField(null=True)

    def __str__(self):
        return self.name