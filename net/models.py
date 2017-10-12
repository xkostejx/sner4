# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Net(models.Model):
    cidr = models.CharField(max_length=39, verbose_name="CIDR")
    ip_first = models.GenericIPAddressField(verbose_name="First IP")
    ip_last = models.GenericIPAddressField(verbose_name="Last IP")
    organization = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    note = models.CharField(max_length=200)

