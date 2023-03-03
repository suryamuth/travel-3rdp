from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from . models import place,team

# Create your views here.
def home(request):
    obj=place.objects.all()
    tobj=team.objects.all()
    return render(request,"index.html",{'places':obj,'teams':tobj})



def contact(request):
    return render(request,"contact.html")