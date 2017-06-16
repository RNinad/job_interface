from django.conf.urls import url

from . import views 

urlpatterns = [
	url(r'^$', views.index, name= 'index'),	
	url(r'^create_jobs/$', views.createJobs, name= 'cjobs'),
	url(r'^jobcreator/$', views.jobCreator),
	url(r'^display_jobs/$', views.displayJobs, name= 'djobs'),
	url(r'^applications/$', views.dispApplications, name= 'applications'),
	url(r'^application_creator/$', views.appCreator),
	url(r'^apply/$', views.apply, name= 'apply'),
	url(r'^submit_application/$', views.submitApplication, name= 'submitapp'),
	url(r'^status_toggle', views.statusToggle),
	url(r'^status/$', views.dispStatus, name= 'status'),
	url(r'^login/$', views.login, name='login'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^asignup/$', views.applicant_signUpHandler),
	url(r'^csignup/$', views.company_signUpHandler),
	url(r'^login/home/$', views.logInHandler),
	url(r'^home/$', views.homeRenderer),

]