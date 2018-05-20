from django.conf.urls import url

from .views import News

urlpatterns = [
    url(r'^(?P<id>\d+)$', News.as_view(), name='post'),
]
