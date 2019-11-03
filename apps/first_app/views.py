from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
from datetime import datetime

# Create your views here

def index(request):
    context = {
        "time": strftime("%b %d, %Y \n %H:%M %p", gmtime()),
        "now": datetime.now()
    }
    return render(request, 'first_app/index.html', context)
