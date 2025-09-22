
from django.db import models
from students.models import Student
from classes.models import Class

class Attendance(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	date = models.DateField()
	period = models.CharField(max_length=20, blank=True, null=True)
	status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent'), ('leave', 'Leave')])
	class_ref = models.ForeignKey(Class, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.student} - {self.date} - {self.status}"
