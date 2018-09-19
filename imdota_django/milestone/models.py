from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=20)
    logo = models.FileField()

class Championship(models.Model):
    year = models.DateField('YYYY')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)



