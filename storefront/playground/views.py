from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@require_http_methods(['GET','POST'])

def hook_receiver(request):
    if request.method == 'POST':
        return HttpResponse("Webhook received!")
    if request.method == 'GET':
        return HttpResponse("GET Request Successful")