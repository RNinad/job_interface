from django.conf.urls import url

from . import views 

urlpatterns = [
	url(r'^$', views.index, name= 'index'),	
	url(r'^create_jobs/$', views.createJobs, name= 'cjobs'),
	url(r'^display_jobs/$', views.displayJobs, name= 'djobs'),
	url(r'^applications/$', views.dispApplications, name= 'applications'),
	url(r'^apply/$', views.apply, name= 'apply'),
	url(r'^submit_application/$', views.submitApplication, name= 'submitapp'),
	url(r'^status/$', views.dispStatus, name= 'status'),
]