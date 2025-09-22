
from django.db import models
from classes.models import Class
from students.models import Student

class Exam(models.Model):
	name = models.CharField(max_length=100)
	class_ref = models.ForeignKey(Class, on_delete=models.CASCADE)
	date = models.DateField()

	def __str__(self):
		return f"{self.name} - {self.class_ref}"

class Mark(models.Model):
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.CharField(max_length=50)
	marks_obtained = models.FloatField()
	max_marks = models.FloatField()

	def __str__(self):
		return f"{self.student} - {self.exam} - {self.subject}"
