# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Job

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['params', 'status', 'result', 'result_data', 'agentid', \
                  'created', 'finished', 'priority']
