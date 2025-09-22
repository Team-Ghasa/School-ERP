
from django.db import models


class Subject(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name

class Class(models.Model):
	name = models.CharField(max_length=50, unique=True)
	section = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return f"{self.name} - {self.section}" if self.section else self.name

class ClassSubject(models.Model):
	class_ref = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subjects')
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return f"{self.class_ref} - {self.subject} - {self.teacher}" 
