import time 
from celery import shared_task
from django.contrib.auth.models import User



@shared_task
def add (**info) :

    print(info)
    pass


# @shared_task
# def create_u(name,pas) : 

#     return name + pas