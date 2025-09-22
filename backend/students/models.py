
from django.db import models
from users.models import User
from parents.models import Parent
from classes.models import Class
from sections.models import Section

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
	admission_no = models.CharField(max_length=20, unique=True)
	student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
	section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
	parent = models.ForeignKey('parents.Parent', on_delete=models.SET_NULL, null=True, related_name='children')

	def __str__(self):
		return f"{self.user.get_full_name()} ({self.admission_no})"
