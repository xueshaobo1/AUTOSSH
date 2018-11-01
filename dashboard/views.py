# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import redirect
from django.http import HttpResponse
from . import models

def index(request):
	on = models.device.objects.filter(state=1).count()
	off = models.device.objects.filter(state=0).count()
	dev_count = models.device.objects.all().count()
	user_count = models.user.objects.all().count()
	user = models.user.objects.all()
	device = models.device.objects.all()
	return render(request, 'index.html',locals())