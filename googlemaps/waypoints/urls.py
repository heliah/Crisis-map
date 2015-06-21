from django.conf.urls import *
urlpatterns = patterns('googlemaps.waypoints.views',
                       url(r'^$','index',name='waypoints_index'),
                       url(r'^save$', 'save', name='waypoints_save'),
                       ) 