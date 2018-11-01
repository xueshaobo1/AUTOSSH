# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import models

def my_login(func):
	def check_login(request):
		if request.session.has_key('user_id'):
			return func(request)
		else:
			return redirect('/account/login/')
	return check_login

def login(request):
	if request.session.get('is_login',None):
		return redirect('/dashboard/index/')
	if request.method == "POST":
		useremail = request.POST.get('email')
		password = request.POST.get('password')
		if useremail and password:
			try:
				user = models.user.objects.get(email = useremail)
			except:
				return render(request,'login.html')
			if password == user.password:
				request.session['is_login'] = True
				request.session['user_id'] = user.id
				request.session['user_name'] = user.name
				return redirect('/dashboard/index/')
	return render(request, 'login.html')

def logout(request):
	if not request.session.get('is_login',None):
		return redirect('/dashboard/index/')
	request.session.flush()
	return redirect('/dashboard/index/')

def user(request):
	user_name = models.user.objects.all()
	user_group = models.group.objects.all()
	return render(request, 'user.html',locals())

def user_add(request):
	if request.method == "POST":
		add_user = request.POST.get('name')
		add_email = request.POST.get('email')
		add_password = request.POST.get('password')
		add_introduce = request.POST.get('introduce')
		add_group = request.POST.get('group')
		group = models.group.objects.get(name=add_group)
		add = models.user.objects.create(name=add_user,email=add_email,password=add_password,introduce=add_introduce,user_group=group)
		return redirect('/account/user/')

def user_del(request):
	try:
		idlist = request.GET['id']
		for i in idlist.split(','):
			info = models.user.objects.get(id=i).delete()
			return redirect('/account/user/')
	except:
		return redirect('/account/user/')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
