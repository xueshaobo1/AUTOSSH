# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import models

def dev_index(request):
	user_group = models.group.objects.all()
	device_name = models.device.objects.all()
	return render(request, 'dev_index.html',locals())
	
def dev_add(request):
	if request.method == "POST":
		add_hname = request.POST.get('hostname')
		add_ip = request.POST.get('ip')
		add_uname = request.POST.get('username')
		add_password = request.POST.get('password')
		add_port = request.POST.get('port')
		add_position = request.POST.get('position')
		add_introduce = request.POST.get('introduce')
		add_group = request.POST.get('group')
		group = models.group.objects.get(name=add_group)
		add = models.device.objects.create(hostname=add_hname,ip=add_ip,link="SSH",username=add_uname,password=add_password,port=add_port,position=add_position,introduce=add_introduce,state=False,user_group=group)
		return redirect('/device/dev_index/')

def dev_edit(request):
	if request.method == "POST":
		up_id = request.POST.get('dev_id')
		up_hname = request.POST.get('dev_hname')
		up_position = request.POST.get('dev_position')
		up_introduce = request.POST.get('dev_introduce')
		up_group = request.POST.get('dev_group')
		group = models.group.objects.get(name=up_group)
		up = models.device.objects.get(id=up_id)
		up.hostname = up_hname
		up.position = up_position
		up.introduce = up_introduce
		up.group = group
		up.save()
		return redirect('/device/dev_index/')
		
def dev_del(request):
	try:
		idlist = request.GET['id']
		for i in idlist.split(','):
			info = models.device.objects.get(id=i).delete()
			return redirect('/device/dev_index/')
	except:
		return redirect('/device/dev_index/')