# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Applicant, Company, Job, Application

from .constants import SECTORS, DEPARTMENTS
         
# Create your views here.
class Current_user:
	def set_user(self, user, utype):
		self.user= user
		self.type= utype

	def current_user(self):
		return self.user
cu =Current_user()
def index(request):
	global cu
	cu = None
	return render(request, 'index.html', {})


def login(request):
	return render(request, 'login.html',{})

def signup(request):
	return render(request,'signup.html',{'sectors': SECTORS})

def logInHandler(request):
	global cu
	cu = Current_user()
	uemail= request.POST['uemail']
	pw= request.POST['password']
	utype= request.POST.get('utype')

	found= False
	
	if utype == 'applicant':
		users= tuple(Applicant.objects.all())	
	elif utype == 'company':
		users= tuple(Company.objects.all())
	global u_type
	u_type = utype
	for user in users:
		if user.email == uemail:
			if user.password == pw:
				found= True
				break

	if( found== True):
		cu.set_user(user, utype)
		return redirect('/naukri/home/')
	else:
		#error message
		pass


def homeRenderer(request):
	return render(request, 'home.html', {'utype':u_type})

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

def createJobs(request):
	return render(request, 'createJobs.html', {'departments':DEPARTMENTS})

def jobCreator(request):
	dept= request.POST['department']
	qual= request.POST['qualification']
	exp= request.POST['experience']
	loc= request.POST['location']
	global cu

	job = Job(company_providing_job= cu.user,job_sector= cu.user.sector, department= dept, qualifications= qual, experience= exp, location= loc )
	job.save()

	return redirect("/naukri/home/")


def displayJobs(request):
	l= tuple(Job.objects.all())
	return render(request, 'displayJobs.html', {'jobs':l})

def dispApplications(request):
	applications = Application.objects.all()
	departments = []
	for application in applications:
		departments.append(application.job.department)
	return render(request, 'displayApplications.html', {'applications':applications, 'departments':departments})

def apply(request):
	global cu
	return render(request, 'apply.html', {'applicant':cu.user, 'department_list':DEPARTMENTS,'sectors':SECTORS})

def submitApplication(request):
	dept = request.POST['dept']
	sect = request.POST['sect']
	global jobs 
	jobs = []
	for job in Job.objects.all():
		if job.department == dept and job.company_providing_job.sector == sect:
			jobs.append(job)
	return render(request, 'submitApplication.html', {'jobs':jobs})

def appCreator(request):
	global cu, jobs
	job_list = request.POST.getlist('joblist[]')
	for job in jobs:
		if job.company_providing_job.username in job_list:
			a = Application(job= job, applicant= cu.user, status= 'standby')
			a.save()
	return redirect('/naukri/home')

def statusToggle(request):
	pass

def dispStatus(request):
	return render(request, 'displayStatus.html', {})


