from django.shortcuts import render, redirect
from .models import Messages


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        Messages.objects.create(name=request.POST['fullname'], email=request.POST['email'],
                                    subject=request.POST['subject'], message=request.POST['message'])
    return render(request, 'contact.html')

