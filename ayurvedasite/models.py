
from django.db import models
from django.utils import timezone
from django.conf import settings

class Symptoms(models.Model):
	name=models.CharField(max_length=100)
	image=models.ImageField(upload_to='static/ayurvedasite/images/', default='static/ayurvedasite/images/no.png')
	description=models.TextField(max_length=500)
	causes=models.TextField(max_length=500)
	symptom=models.TextField(max_length=500)
	remedy=models.TextField(max_length=500)
	link=models.URLField(max_length=100)

	def __str__(self):  
		return self.name


		
		
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

