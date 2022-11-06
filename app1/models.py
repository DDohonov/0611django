from django.db import models

class First_model(models.Model):
    title = models.CharField(max_length = 255, default = "")