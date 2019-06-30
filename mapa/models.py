# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=400, default=0)
	latitud = models.FloatField(null=True, blank=True, default=None)
	longitud = models.FloatField(null=True, blank=True, default=None)

	def __str__(self):
		return self.title