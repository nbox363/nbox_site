from django.views.generic import DetailView, ListView

from .models import Articles


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
