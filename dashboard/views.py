# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import redirect
from django.http import HttpResponse
from . import models

def index(request):
	
	return render(request, 'index.html')