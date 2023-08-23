from django.shortcuts import render, HttpResponse
from app import tasks 


def home (request) : 
    
    res = tasks.add.delay(username='radwan')
    print('sent to celery')


    return HttpResponse('Done')
