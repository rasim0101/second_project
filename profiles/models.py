from django.db import models

def movie_images_upload(instance, filename):
	return f"movie{instance.movie.id}/{filename}"

class Movie(models.Model):
	name = models.CharField(max_length=60, verbose_name='Название фильма')
	description = models.TextField(verbose_name='Краткий сюжет')
	release_date = models.DateField(verbose_name='Дата выхода')

	def __str__(self):
		return f"{self.name} {self.release_date}"


	class Meta:
		verbose_name='Фильм'
		verbose_name_plural='Фильмы'


class MovieImage(models.Model):
	file = models.ImageField(upload_to=movie_images_upload)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

	def __str__(self):
		return self.file.url

	class Meta:
		verbose_name='Изображение к фильму'
		verbose_name_plural='Изображения к фильму'