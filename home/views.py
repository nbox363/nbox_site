from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home/home_page.html')


def contact(request):
    return render(request, 'home/contact_page.html', {'values': ['По всем вопросам:', '+363 363 364']})


def about(request):
    return render(request, 'home/about.html')
