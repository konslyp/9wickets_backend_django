from django.db import models

class Sport (models.Model):
    name = models.CharField(primary_key=True,max_length = 50)
    sport_id= models.IntegerField()
    market_count = models.IntegerField()

    def __str__(self):
        return self.name
