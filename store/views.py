from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone


def hello_world(request):
    current_time =  timezone.now()
    # 'he'
    return  HttpResponse(current_time)
