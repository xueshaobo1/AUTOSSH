from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^dev_index/', views.dev_index),
	url(r'^dev_add/', views.dev_add),
	url(r'^dev_edit/', views.dev_edit),
	url(r'^dev_del/', views.dev_del),
]

