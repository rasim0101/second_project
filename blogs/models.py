from django.db import models
from profiles.models import Profile

class Blog(models.Model):
	title = models.CharField(max_length=200)
	authors = models.ManyToManyField(Profile)

	def __str__(self):
		return self.title
