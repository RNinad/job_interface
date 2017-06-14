# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Applicant, Company, Job, Application

from .constants import SECTORS
         
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

class Current_user:
	def __init__(self):
		self.user= Applicant(username= 'dummy')

	def set_user(self, obj, utype):
		self.user= obj
		self.type= utype

	def current_user(self):
		return self.user

cu= Current_user()

def login(request):
	return render(request, 'login.html',{})

def signup(request):
	return render(request,'signup.html',{'sectors': SECTORS})

def logInHandler(request):
	email= request.POST['email']
	pw= request.POST['password']
	utype= request.POST.get('utype')

	found= False
	
	if utype == 'applicant':
		users= tuple(Applicant.objects.all())	
	elif utype == 'company':
		users= tuple(Company.objects.all())

	for user in users:
		if user.email == email:
			if user.password == pw:
				found= True
				break

	if( found== True):
		cu.set_user(user, utype)
		return render(request, 'home.html', {'utype':utype})
	else:
		#error message
		pass

def company_signUpHandler(request):
	un=	 request.POST['username']
	pw=  request.POST['password']
	email=  request.POST['email']
	sector= request.POST['sector']
	reg=  request.POST['registration_no']
	web= request.POST['website']
	ph= request.POST['phone_no']

	user= Company(username=un, password=pw, email=email, sector=sector, registration_no =reg, website= web, phone_no =ph)
	user.save()
	return login(request)


def applicant_signUpHandler(request):
	un= request.POST['username']
	pw= request.POST['password']
	email= request.POST['email']
	dob= request.POST['date']
	gender= request.POST['gender']
	qual= request.POST['qual']
	mob= request.POST['mobile']

	applicant= Applicant(username= un, password=pw, email=email, DOB= dob, gender= gender, broad_qualification= qual, mobile_no= mob)
	applicant.save()
	return login(request)
