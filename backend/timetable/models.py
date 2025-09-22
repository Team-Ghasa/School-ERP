
from django.db import models
from classes.models import Class
from teachers.models import Teacher

class Timetable(models.Model):
	class_ref = models.ForeignKey(Class, on_delete=models.CASCADE)
	day = models.CharField(max_length=10)
	period = models.CharField(max_length=20)
	subject = models.CharField(max_length=50)
	teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return f"{self.class_ref} {self.day} {self.period}"
