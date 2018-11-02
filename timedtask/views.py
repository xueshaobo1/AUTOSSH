# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import models
import os


def shell(request):
	s = os.path.join((os.getcwd()),'shell')
	shell_list = os.listdir(s)
	return render(request, 'shell.html',locals())

def add_shell(request):
	if request.method == "POST":
		shell_name = request.POST.get('name')
		shell_body = request.POST.get('body')
		pwd = os.path.join((os.getcwd()),'shell',shell_name)
		f = open(pwd,'w+')
		p = f.write(shell_body)
		f.close()
		return redirect('/timedtask/shell/')

def del_shell(request):
	if request.method == "POST":
		shell_name = request.POST.get('name')
		os.remove(os.path.join((os.getcwd()),'shell',shell_name))
		return redirect('/timedtask/shell/')

def task(request):
	task_name = os.system("crontab -l")
	print task_name
	return render(request, 'task.html',locals())