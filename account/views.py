# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import models

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
	
