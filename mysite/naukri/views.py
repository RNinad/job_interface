# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def createJobs(request):
	return render(request, 'createJobs.html', {})
	
def displayJobs(request):
	return render(request, 'displayJobs.html', {})

def dispApplications(request):
	return render(request, 'displayApplications.html', {})

def apply(request):
	return render(request, 'apply.html', {})

def submitApplication(request):
	return render(request, 'submitApplication.html', {})

def dispStatus(request):
	return render(request, 'displayStatus.html', {})