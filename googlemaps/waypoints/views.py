from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from pip._vendor import requests
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
from googlemaps.waypoints.models import Waypoint, Report
import simplejson
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from datetime import datetime
from Crypto.Random.random import randint

#===============================================================================
# def index(requests):
#     'Display Map'
#     return render_to_response('waypoints/index.html',{
#                                                       
#                                                       })
#===============================================================================

def index(request):
    'Display map'
    waypoints = Waypoint.objects.order_by('name')
    reports = Report.objects.order_by('id')
    return TemplateResponse(request, 'waypoints/index.html', {
        'reports': reports,
        'waypoints': waypoints,
        'content': render_to_string('waypoints/waypoints.html',{'waypoints': waypoints, 'reports': reports,}),
    })
# Create your views here.
@csrf_exempt
def save(request):
    'Save waypoints'
    for waypointString in request.POST.get('waypointsPayload', '').splitlines():
        waypointID, waypointX, waypointY = waypointString.split()
        waypoint = Waypoint.objects.get(id=int(waypointID))
        #rg = 'POINT(' + str(waypointX) + ' ' + str(waypointY) + ')'
        #Report(reportCategory='1', reportDetails='serious', reportGeometry=rg).save()
        waypoint.geometry.set_x(float(waypointX))
        waypoint.geometry.set_y(float(waypointY))
        waypoint.save()
    for reportString in request.POST.get('reportPayload', '').splitlines():
        reportCat, reportX, reportY  = reportString.split()
        reportDet = request.POST.get('detailsAdded', '')
        if reportDet == "test-val":
            for x in range(0, 3000):
                down = 35.6645 + randint(0,1100) * 0.0001
                print down
                left = 51.2292 + randint(0,3600) * 0.0001
                #print left
                tp = 'POINT(' + str(left) + ' ' + str(down) + ')'
                Report(reportCategory='2', reportDetails='test value', reportGeometry=tp).save()
            for x in range(0, 1000):
                down = 35.6645 + randint(0,1100) * 0.0001
                print down
                left = 51.2292 + randint(0,3600) * 0.0001
                #print left
                tp = 'POINT(' + str(left) + ' ' + str(down) + ')'
                Report(reportCategory='1', reportDetails='test value', reportGeometry=tp).save()
            for x in range(0, 100):
                down = 35.6645 + randint(0,1100) * 0.0001
                print down
                left = 51.2292 + randint(0,3600) * 0.0001
                #print left
                tp = 'POINT(' + str(left) + ' ' + str(down) + ')'
                
            for x in range(0, 10):
                down = 35.6645 + randint(0,1100) * 0.0001
                print down
                left = 51.2292 + randint(0,3600) * 0.0001
                #print left
                tp = 'POINT(' + str(left) + ' ' + str(down) + ')'
                Report(reportCategory='4', reportDetails='test value', reportGeometry=tp).save()
        rg = 'POINT(' + str(reportX) + ' ' + str(reportY) + ')'
        Report(reportCategory=reportCat, reportDetails=reportDet, reportGeometry=rg).save()
    return HttpResponse(simplejson.dumps(dict(isOk=1)), mimetype='application/json')







