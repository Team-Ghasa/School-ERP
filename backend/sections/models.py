
from django.db import models

class Section(models.Model):
	name = models.CharField(max_length=20)
	class_ref = models.ForeignKey('classes.Class', on_delete=models.CASCADE, related_name='sections')

	def __str__(self):
		return f"{self.class_ref.name} - {self.name}"
