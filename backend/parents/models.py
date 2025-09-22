
from django.db import models
from users.models import User

class Parent(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_profile')

	def __str__(self):
		return f"{self.user.get_full_name()} (Parent)"
