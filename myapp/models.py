from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Puzzle types, from 3x3 to 5x5
class Puzzle(models.Model):
    PUZZLE = [
    ("2","2x2"),
    ("3","3x3"),
    ("4","4x4"),
    ("5","5x5")
    ]

    puzzleID = models.AutoField(primary_key=True)
    puzzleType = models.CharField(blank=True,max_length=1,choices=PUZZLE)

    def __str__(self):
        return self.puzzleType+ "x" + self.puzzleType 


# Scrambles in relation to the puzzle type
class Scramble(models.Model):
    scrambleID = models.AutoField(primary_key = True)
    scrambleType = models.ForeignKey(Puzzle, on_delete=models.CASCADE,blank=True,null=True  )
    scramble = models.CharField(blank=True, max_length=45)
