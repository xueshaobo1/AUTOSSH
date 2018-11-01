from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^$', views.login),
	url(r'^login/', views.login),
	url(r'^logout/', views.logout),
	url(r'^user/', views.user),
	url(r'^user_add/', views.user_add),
	url(r'^user_del/', views.user_del),
	
]
