from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^shell/', views.shell),
	url(r'^add_shell/', views.add_shell),
	url(r'^del_shell/', views.del_shell),
	url(r'^task/', views.task),
]

