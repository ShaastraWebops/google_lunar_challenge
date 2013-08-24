from django.conf.urls import patterns, include, url
from authmn import views

urlpatterns = patterns('',
	
	url('^register/$',views.register),
	url('^login/$',views.login),
	url('^edit_profile/$',views.edit_profile,name='authmn_edit_profile'),
	url('^edit_user_profile/$',views.edit_user_profile,name='authmn_edit_user_profile'),
    url('^lunar_first_round/$',views.lunar_first_round),
	url('^logout/$',views.logout,name='authmn_logout'),
	url('^home/$',views.home),
)
