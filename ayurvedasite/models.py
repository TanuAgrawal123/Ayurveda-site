
from django.db import models
from django.utils import timezone
from django.conf import settings


class Comment(models.Model):
	user=models.CharField(max_length=200)
	email=models.EmailField()
	text=models.TextField(max_length=500)
	created_date=models.DateTimeField(default=timezone.now())
	approved_comment=models.BooleanField(default=False)

	def approve(self):
		self.approved_comment=True
		self.save()

	def ___str__(self):

		return self.text

