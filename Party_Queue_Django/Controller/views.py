from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Controller.functions import post_next_song, get_next_song
from Controller.models import Song

# For testing with PostMan
@csrf_exempt

# POST Function - for json song files 
@require_http_methods('POST')
def post_song(postJson):
    return HttpResponse(post_next_song(postJson))

# GET Function - for json song files
@require_http_methods('GET')
def get_song(request):
    return HttpResponse(get_next_song())

