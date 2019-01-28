from django.db import models

class User (models.Model):
    name = models.CharField(primary_key=True,max_length = 50)
    pw = models.CharField(max_length = 255)
    type = models.IntegerField()
    credit = models.FloatField()

    def __str__(self):
        return self.name
