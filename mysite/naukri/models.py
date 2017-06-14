# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Company(models.Model):
	username= models.CharField(max_length=20)
	password= models.CharField(max_length=20)
	email= models.CharField(max_length=40)
	sector= models.CharField(max_length=100)
	registration_no= models.CharField(max_length=30)
	website= models.CharField(max_length=40)
	phone_no= models.CharField(max_length=13)

	def __str__(self):
		return self.username


class Applicant(models.Model):
	username= models.CharField(max_length=20)
	password= models.CharField(max_length=20)
	email= models.CharField(max_length=40)
	DOB= models.CharField(max_length=12)
	gender= models.CharField(max_length=7)
	broad_qualification= models.CharField(max_length=10)
	mobile_no= models.CharField(max_length=12)

	def __str__(self):
		return self.username

class Job(models.Model):
	company_providing_job= models.ForeignKey(Company)
	job_sector= models.CharField(max_length=20)
	department= models.CharField(max_length=20)
	qualifications= models.CharField(max_length=40)
	experience= models.CharField(max_length=40)
	location= models.CharField(max_length=15)

class Application(models.Model):
	applicant= models.ForeignKey(Applicant)
	job=  models.ForeignKey(Job)
	status= models.CharField(max_length=8)

	def __str__(self):
		return self.status