from django.db import models

class Data(models.Model):
  json_data=models.JSONField()
