from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
	def create_user(self,email,username,password=None):
		if not email:
			raise ValueError("Users must have an email address")
		if not username:
			raise ValueError("Users must have a username")

		user = self.model(
			email = self.normalize_email(email), # lowercase conversion
			username = username,
		)	
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,username,password):
		user = self.create_user(
				email = self.normalize_email(email), # lowercase conversion
				username = username,
				password = password,
			)
		user.is_admin=True
		user.is_staff=True
		user.is_superuser=True
		user.save(using=self._db)
		return user			

class Account(AbstractBaseUser):
	email = models.EmailField(verbose_name='email', max_length=60, unique=True)
	username = models.CharField(max_length=30, unique=True)
	date_joined = models.DateTimeField(verbose_name='date_joined',auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last_login',auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'email' #login credential
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager() #reference to account manager

	def __str__(self):
		return self.email

	def has_perm(self,perm,obj=None): #admin permissions
		return self.is_admin

	def has_module_perms(self,app_label):
		return True		

