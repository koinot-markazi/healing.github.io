from django.db import models

class MainPage(models.Model):
	telnumber = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	contacts_description = models.TextField()
	facebook_link = models.CharField(max_length=255)
	twitter_link = models.CharField(max_length=255)
	instagram_link = models.CharField(max_length=255)