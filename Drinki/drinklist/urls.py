from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from drinklist.models import Drink,DrinkComments
from . import views


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Drink.objects.all().order_by("-data")[:25],
                                template_name="drinklist/drinks.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Drink,
                                             template_name= 'drinklist/drink.html')),
    
    url(r'^new/$', views.post_new, name='post_new'),
    ]
