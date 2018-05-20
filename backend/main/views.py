from django.shortcuts import render
from django.views.generic.list import ListView

from news.models import News
from .models import MainPage

class Home(ListView):

	template_name="index.html"
	model = MainPage
	context_object_name = 'page'

	def get_queryset(self):
		qs = super().get_queryset() 
		return qs.first()

	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['news'] = News.objects.all().order_by('-id')[:3]
		return context