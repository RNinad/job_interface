# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Applicant, Company, Job, Application
         
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

class current_user:
	def __init__(self):
		self.user= Applicant(username= 'dummy')

	def set_user(self, obj):
		self.user= obj

	def current_user(self):
		return self.user

cu= current_user()

def login(request):
	return render(request, 'login.html',{})

def signup(request):
	return render(request,'signup.html',{})

def logInHandler(request):
	email= request.POST['email']
	pw= request.POST['password']

	users= tuple(Applicant.objects.all())
	found= False

	for user in users:
		if user.email == email:
			if user.password == pw:
				found= True
				break

	#print user
	#print '\n\n'

	if( found== True):
		cu.set_user(user)

		return render(request, 'home.html', {})
	else:
		#error message
		pass
		
def signup(request):
	return render(request, 'signup.html', {})

def Company_signUpHandler(request):
	un=	 request.POST['username']
	pw=  request.POST['password']
	email=  request.POST['email']
	sector= request.POST['']
	reg=  request.POST['registration_no']
	web= request.POST['website']
	ph= request.POST['phone_no']

	user= Company(username=un, password=pw, email=email, sector=sector, registration_no =reg, website= web, phone_no =ph)
	user.save()
	login(request)
	
