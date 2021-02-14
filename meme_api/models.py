from django.db import models

class MemeModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    caption = models.CharField(max_length=200, blank=False)
    url = models.URLField(max_length=200, blank=False)

    def __str__(self):
        return self.name