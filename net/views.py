# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import NetForm
from .models import Net

def index(request):
#    return HttpResponse("New project!")
     return redirect(net_list)

def net_list(request, template_name='net/list.html'):
    nets = Net.objects.all()
    data = {}
    data['net_list'] = nets
    return render(request, template_name, data)

def net_add(request, template_name='net/addedit.html'):
    form = NetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(net_list)
    return render(request, template_name, {'form':form})

def net_edit(request, pk, template_name='net/addedit.html'):
    net = get_object_or_404(Net, pk=pk)
    form = NetForm(request.POST or None, instance=net)
    if form.is_valid():
        form.save()
        return redirect(net_list)
    return render(request, template_name, {'form':form})

def net_delete(request, pk):
    net = get_object_or_404(Net, pk=pk)    
    if request.method=='POST':
        net.delete()
    return redirect(net_list)
# Create your views here.
