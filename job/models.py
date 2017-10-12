# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime  
from django.contrib.postgres.fields import JSONField


class Job(models.Model):
    STATUS_NEW = 0
    STATUS_ASSIGNED = 1
    STATUS_DONE = 2
    STATUS_TIMEOUT = 3
    STATUS_CHOICES = (
                (STATUS_NEW, 'New'), 
                (STATUS_ASSIGNED, 'Assigned'),
                (STATUS_DONE, 'Done'), 
                (STATUS_TIMEOUT, 'Timeout')
    )

    taskid = models.PositiveIntegerField(default=0, primary_key=False)
    params = JSONField(verbose_name="Params")
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_NEW, verbose_name="Status")
    result = models.CharField(max_length=64, verbose_name="Result")
    result_data = models.CharField(max_length=64, verbose_name="Result data")
    agentid = models.CharField(max_length=32, verbose_name="Agent ID")
    created = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Created") 
    finished = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Finished')
    priority = models.PositiveSmallIntegerField(verbose_name="Priority")
