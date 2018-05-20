from django.conf.urls import url

from .views import save

urlpatterns = [
    url(r'^$', save, name='save'),
]
