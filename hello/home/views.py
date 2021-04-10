from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from home.models import Chat
from home.models import Chat1

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

def chat(request):
    if request.method == "POST":
        email1 = request.POST.get ('email1')
        email2 = request.POST.get ('email2')
        email3 = request.POST.get ('email3')
        email4 = request.POST.get ('email4')
        chat = Chat(email1=email1,email2=email2,email3=email3,email4=email4)
        chat.save()
        
    return render(request, 'Chat.html')

def chat1(request):
    if request.method == "POST":
        email = request.POST.get('email')
        chat1 = Chat1(email=email)
        chat1.save()
    return render(request, 'chat1.html')

