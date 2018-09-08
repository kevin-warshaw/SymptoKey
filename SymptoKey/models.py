from django.db import models

# Create your models here.

class Symptoms(models.Model):
    dizzy = models.BooleanField(default=False)
    visiblyBleeding = models.BooleanField(default=False)
    difficultyBreathing = models.BooleanField(default=False)


class Profile(models.Model):
    isMale = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    risk = models.IntegerField(default=0)