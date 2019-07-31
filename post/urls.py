from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('index/', post_index, name='index'),
    path('create/', post_create, name='create'),
    path('<slug:slug>/', post_detail, name='detail'),
    path('<slug:slug>/update', post_update, name='update'),
    path('<slug:slug>/delete', post_delete, name='delete'),]

#urlpatterns = [

#    url(r'^index/$', post_index, name="index"),

#    url(r'^create/$', post_create, name='create'),

#    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),

#    url(r'^(?P<slug>[\w-]+)/update/$', post_update, name="update"),

#    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),]