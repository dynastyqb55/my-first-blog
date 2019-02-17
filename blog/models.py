from django.conf import settings 
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
 	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
 	title = models.CharField(max_length=200)
 	time = models.IntegerField(null=True, blank=True)
 	description = models.TextField(null=True)
 	ingredients = models.TextField(null=True)
 	steps = models.TextField(null=True)
 	published_date = models.DateTimeField(blank=True, null=True)

 	def publish(self): 
 		self.published_date = timezone.now()
 		self.save()

 	def __str__(self):
 		return self.title





















