# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import NetForm
from .models import Net

def index(request):
#    return HttpResponse("New project!")
     return redirect(netmap_list)

def netmap_list(request, template_name='list.html'):
    nets = Net.objects.all()
    data = {}
    data['net_list'] = nets
    return render(request, template_name, data)

def netmap_add(request, template_name='addedit.html'):
    form = NetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(netmap_list)
    return render(request, template_name, {'form':form})

def netmap_edit(request, pk, template_name='addedit.html'):
    netmap = get_object_or_404(Net, pk=pk)
    form = NetForm(request.POST or None, instance=netmap)
    if form.is_valid():
        form.save()
        return redirect(netmap_list)
    return render(request, template_name, {'form':form})

def netmap_delete(request, pk):
    netmap = get_object_or_404(Net, pk=pk)    
    if request.method=='POST':
        netmap.delete()
    return redirect(netmap_list)
# Create your views here.
