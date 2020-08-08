from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect

from .forms import ArticlesForm
from .models import Articles


def article_create_view(request):
    form = ArticlesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('articles')

    context = {
        'form': form
    }

    return render(request, 'articles/article_create_page.html', context)


class ArticleView(DetailView):
    template_name = 'articles/article_page.html'
    model = Articles

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['article'] = Articles.objects.all()
        return context


class ArticlesView(ListView):
    template_name = 'articles/articles_page.html'

    def get_queryset(self):
        return Articles.objects.all().order_by('-date')[:5]

    def get_context_data(self, *args, **kwargs):
        contex = super().get_context_data(*args, **kwargs)
        contex['articles'] = Articles.objects.all()
        return contex
