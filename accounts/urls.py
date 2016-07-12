from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout,{'next_page':'home'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup')
]
