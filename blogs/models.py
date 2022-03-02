from django.db import models
from profiles.models import Profile
from django.urls import reverse
from slugify import slugify
from ckeditor.fields import RichTextField



class Blog(models.Model):
	title = models.CharField(max_length=200)
	text = RichTextField(null=True)
	authors = models.ManyToManyField(Profile)
	slug = models.SlugField(null=True)

	def get_absolute_url(self):
		return reverse('blog_detail', kwargs={'slug':self.slug})

	def save(self, *args, **kwargs):
		self.slug=slugify(self.title)
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.title


class Comment(models.Model):
	text = models.TextField()
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.text[:20]

	def get_absolute_url(self):
		return reverse('comment_detail', args=[str(self.id)])

	

