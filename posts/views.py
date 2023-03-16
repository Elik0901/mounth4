from django.shortcuts import HttpResponse, redirect
from datetime import datetime
# Create your views here.

def hello_v(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")

def youtube_veiw(request):
    if request.method == 'GET':
        return redirect("https://www.youtube.com")

def google_veiw(request):
    if request.method == 'GET':
        return redirect("https://www.google.com")

def now_date(request):
    if request.method == 'GET':
        time = datetime.now()
        return HttpResponse(time)

def goodbay(request):
    if request.method == 'GET':
        return HttpResponse("Goodbay user")

