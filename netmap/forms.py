# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Net

class NetForm(ModelForm):
    class Meta:
        model = Net
        fields = ['cidr', 'ip_first', 'ip_last', 'organization', 'description', 'note']
