from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = { 'queue_name': 'TEST' }
    return render(request, 'dashboard/index.html', context)

def detail(request, queue_name):
    return HttpResponse("> %s." % queue_name)

def results(request, queue_name):
    response = "> %s."
    return HttpResponse(response % queue_name)

def vote(request, queue_name):
    return HttpResponse("> %s." % queue_name)