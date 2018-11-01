# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class group(models.Model):
	name = models.CharField(max_length=128, unique=True)
	introduce = models.CharField(max_length=256)

class user(models.Model):
	name = models.CharField(max_length=128)
	email = models.CharField(max_length=128, unique=True)
	password = models.CharField(max_length=128)
	introduce = models.CharField(max_length=256)
	user_group =  models.ForeignKey('group')
