from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from .models import News as News_model
from main.models import MainPage

class News(DetailView):
	template_name = "news.html"

	def get_object(self):
		return get_object_or_404(News_model, id = self.kwargs['id'])

	def get_context_data(self, **kwargs):
		context = super(News, self).get_context_data(**kwargs)
		context['page'] = MainPage.objects.first()
		context['tags'] = get_object_or_404(News_model, id = self.kwargs['id']).tags.split()
		context['short_news'] = News_model.objects.exclude(id__in=self.kwargs['id']).order_by('-id')[:2]
		return context