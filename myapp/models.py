from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

PUZZLE = [
    ("2","2x2"),
    ("3","3x3"),
    ("4","4x4"),
    ("5","5x5")
    ]


class Statistic(models.Model):
    puzzleType = models.CharField(max_length=10,choices=PUZZLE)
    best = models.BigIntegerField(blank=True)
    average = models.BigIntegerField(blank=True)
    worst = models.BigIntegerField(blank=True)

    class Meta:
       db_table = 'statistic'

class Scramble(models.Model):
	scrambleID = models.AutoField(primary_key=True)
	scrambleLength = models.IntegerField(blank=False)
	scramble = models.CharField(blank=True, max_length=45)

	class Meta:
		db_table = 'scramble'
