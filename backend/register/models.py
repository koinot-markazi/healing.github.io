from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	date = models.CharField(max_length=255)
	department = models.CharField(max_length=255)
	telnumber = models.CharField(max_length=255)
	extra = models.TextField(max_length=255)

	def __str__(self):
		return self.email