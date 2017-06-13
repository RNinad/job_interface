# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Company, Applicant, Job, Application

# Register your models here.
admin.site.register(Company)
admin.site.register(Applicant)
admin.site.register(Job)
admin.site.register(Application)