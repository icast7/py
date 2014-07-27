from django.conf.urls import patterns, include, url
from polls import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#ex:/polls/
	
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^admin/', include(admin.site.urls)),
)
