from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class News(models.Model):
	title = models.CharField(max_length=255)
	tags = models.CharField(max_length=511, help_text='Вводите тэги через пробел')
	short_content = models.TextField(max_length=511)
	content = RichTextUploadingField()
	image = models.ImageField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)
	
	class Meta:
		db_table = "News"
		verbose_name = 'news'
		verbose_name_plural = 'news'

	def __str__(self):
		return self.title