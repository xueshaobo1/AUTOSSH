# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.models import *

class device(models.Model):
	hostname = models.CharField(max_length=128)
	ip = models.CharField(max_length=64,unique=True)
	link = models.CharField(max_length=16)
	username = models.CharField(max_length=32)
	password = models.CharField(max_length=128)
	port = models.IntegerField()
	position = models.CharField(max_length=64)
	introduce = models.CharField(max_length=256)
	state = models.BooleanField(default=False)
	user_group = models.ForeignKey('account.group')
