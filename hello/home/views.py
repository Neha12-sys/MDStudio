from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
   if request.method == "POST":
      email = request.POST.get('email')
      query = request.POST.get('query')
      contact = Contact(email=email, query=query, date=datetime.today())
      contact.save()
   return render(request, 'contact.html')

def services(request):
   return render(request, 'services.html')

def designing(request):
   return render(request, 'designing.html')

def resources(request):
   return render(request, 'resources.html')

def MConnect(request):
   return render(request, 'MConnect.html')
