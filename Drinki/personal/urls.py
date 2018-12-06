from django.conf.urls import url, include
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from django.urls import reverse,reverse_lazy
from . import views
from django.urls import path

from personal.models import ContactMe
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contactme/$', views.contactme, name='contactme'),
    url(r'^contact/$', views.contact_new, name='contact_new'),
    url(r'^register/', CreateView.as_view(template_name='register.html',form_class=UserCreationForm,success_url='/')),
    url(r'^login/', auth_views.login,{'template_name': 'login.html'},name='login'),
    url(r'^logout/', auth_views.logout,{'next_page': reverse_lazy('index')},name='logout'),
      url(r'^wiadomosci/',
        ListView.as_view(
            model=ContactMe,
            context_object_name='wiadomosci',template_name='contactme_list.html'),
        name='wiadomosci'),

]