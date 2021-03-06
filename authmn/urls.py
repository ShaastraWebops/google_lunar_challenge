from django.conf.urls import patterns, include, url
from authmn import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url('^register/$',views.register, name='authmn_register'),
	url('^login/$',views.login, name='authmn_login'),
	url('^edit_profile/$', views.edit_profile, name='authmn_edit_profile'),
	url('^edit_user_profile/$',views.edit_user_profile,name='authmn_edit_user_profile'),
    url('^lunar_first_round/$',views.lunar_first_round),
	url('^logout/$',views.logout,name='authmn_logout'),
	url('^home/$',views.home, name='authmn_home'),
)
