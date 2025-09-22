
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	ROLE_CHOICES = [
		('admin', 'Admin'),
		('teacher', 'Teacher'),
		('student', 'Student'),
		('parent', 'Parent'),
	]
	role = models.CharField(max_length=10, choices=ROLE_CHOICES)

	def __str__(self):
		return f"{self.username} ({self.role})"
from django.db import models
from django.db import models
