from django.shortcuts import render
from django.http import HttpResponse


def works(request):
    return render(request, 'home/works_page.html')

# def works(request):
#     return HttpResponse('Here is will be my works')
