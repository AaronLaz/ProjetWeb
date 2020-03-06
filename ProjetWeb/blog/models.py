from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
# Create your models here.

def upload_location(instance, filename, **kwargs):
	file_path = 'blog/{author_id}/{title}-{filename}'.format(
			author_id = str(instance.author.id), title=str(instance.title), filename=filename
		)
	return file_path

class BlogPost(models.Model):
	title = models.CharField(max_length=50, null=False, blank=False)	
	body = models.TextField(max_length=5000, null=False, blank=False)
	image = models.ImageField(upload_to=upload_location, null=False, blank=False) # needs pillow to be installed (pip install pillow)
	date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # delete objects associated with post, except the author
	slug = models.SlugField(blank=True, unique=True) # url

	def __str__(self):
		return self.title

@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
	instance.image.delete(False) #if blogpost deleted, image is also deleted

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):	#intercepts saving of blogpost before being saved on the DB, to execute action before or after saving
	if not instance.slug:
		instance.slug = slugify(instance.author.username + "-" + instance.title) # create a slug

pre_save.connect(pre_save_blog_post_receiver,sender=BlogPost)		