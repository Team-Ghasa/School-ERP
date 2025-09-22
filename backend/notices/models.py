
from django.db import models
from classes.models import Class

class Notice(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	target_role = models.CharField(max_length=10, choices=[('student', 'Student'), ('parent', 'Parent'), ('teacher', 'Teacher'), ('admin', 'Admin')], blank=True, null=True)
	target_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.title
