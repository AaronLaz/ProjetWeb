from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PUZZLE = [
    ("2","2x2"),
    ("3","3x3"),
    ("4","4x4"),
    ("5","5x5")
    ]

class Scramble(models.Model):
	scrambleID = models.AutoField(primary_key=True)
	scrambleLength = models.IntegerField(blank=False)
	scramble = models.CharField(blank=True, max_length=45)

	class Meta:
		db_table = 'scramble'
