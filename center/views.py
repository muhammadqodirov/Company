from django.shortcuts import render, redirect
from .models import Messages, Courses, Sections


def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html', context={'courses': Courses.objects.all()})

def features(request,id):
    sections = Sections.objects.filter(course_id=id)
    return render(request, 'features.html', context={'sections': sections})


def contact(request):
    if request.method == 'POST':
        Messages.objects.create(name=request.POST['fullname'], email=request.POST['email'],
                                    subject=request.POST['subject'], message=request.POST['message'])
    return render(request, 'contact.html')

