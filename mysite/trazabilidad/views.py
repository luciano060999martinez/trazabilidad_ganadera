from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render 

@login_required()
def index(request):
    return HttpResponse("hola a todos")

    #return HttpResponse("Hello, world. You're at the polls index proyecto holsa.")

