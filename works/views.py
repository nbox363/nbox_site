from django.shortcuts import render
from articles.models import Category


def works(request):
    context = Category.objects.all()
    return render(request, 'works/works_page.html', {'categories': context})

# def works(request):
#     return HttpResponse('Here is will be my works')
