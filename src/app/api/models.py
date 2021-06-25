from django.db import models

# Create your models here.

class News(models.Model):
	title = models.CharField(max_length=50)
	url = models.CharField(max_length=500)
	votes = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)

	# Indicamos el nombre que queremos muestre en el panel
	class Meta:
		verbose_name = "News"
		verbose_name_plural = "News"

	# con esta definicion mostramos el nombre de la pregunta que acabamos de ingresar
	def __str__(self):
		return self.title