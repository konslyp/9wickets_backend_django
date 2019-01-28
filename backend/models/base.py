from django.db import models


class Base (models.Model):
    name = models.CharField(primary_key=True,max_length = 50)
    app_key = models.CharField(max_length = 100)
    session_key = models.CharField(max_length = 100)
    app_id = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
