from django.conf.urls import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
import googlemaps

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'googlemaps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #(r'^admin/', include(admin.site.urls)),
    (r'',include('googlemaps.waypoints.urls')),
)
