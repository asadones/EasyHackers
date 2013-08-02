from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jembauche.views.home', name='home'),
    # url(r'^jembauche/', include('jembauche.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomepageView.as_view(), name='home'),
    url(r'^options/$', OptionsView.as_view(), name='options'),
    url(r'^publish/(?P<job_id>\d+)/$', FinalizeView.as_view(), name='finalize'),
    url(r'^view/(?P<job_id>\d+)/$', EndView.as_view(), name='end'),
)
