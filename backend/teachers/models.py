
from django.db import models
from users.models import User


class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
	qualification = models.CharField(max_length=100, blank=True, null=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	document = models.FileField(upload_to='teacher_docs/', blank=True, null=True)

	def __str__(self):
		return self.user.get_full_name()
