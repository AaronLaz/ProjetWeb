from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class User(models.Model):
    userID = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    userEmail = models.EmailField()

    class Meta:
       db_table = 'user'

class Admin(models.Model):
    adminID = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    adminEmail = models.EmailField()

    class Meta:
       db_table = 'admin'       

class Statistic(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='userID')
    puzzleType = models.CharField(blank=True, max_length=10)
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


class BlogPost(models.Model):
	userID =userID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='userID')
	postName = models.CharField(blank=True, max_length=20)
	postDate = models.DateTimeField(auto_now=False, auto_now_add=False)

	class Meta:
		db_table = 'blogpost'