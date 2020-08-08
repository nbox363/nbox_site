from django.shortcuts import render
from django.http import HttpResponse


def work(request):
    return render(request, 'work/work_page.html')

# def works(request):
#     return HttpResponse('Here is will be my works')
