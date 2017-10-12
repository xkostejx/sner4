# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.shortcuts import render
from .forms import JobForm
from .models import Job

def job_list(request, template_name='job/list.html'):
    jobs = Job.objects.all()
    data = {}
    data['job_list'] = jobs
    return render(request, template_name, data)

def job_add(request, template_name='job/addedit.html'):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(job_list)
    return render(request, template_name, {'form':form})

def job_show(request, pk, template_name='job/addedit.html'):
    job = get_object_or_404(Job, pk=pk)
    form = JobForm(request.POST or None, instance=job)
    return render(request, template_name, {'form':form, 'editable' : False})

def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method=='POST':
        job.delete()
    return redirect(job_list)

def job_getwork(request):
    return HttpResponse(status=501)
