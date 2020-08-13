from django.views.generic import DetailView, ListView, CreateView
from django.shortcuts import reverse
from django.utils.timezone import now
from .forms import ArticlesForm
from .models import Articles


class ArticleView(DetailView):
    template_name = 'articles/article_page.html'
    model = Articles

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['article'] = Articles.objects.all()
    #     context['comments'] = Comments.objects.all()
    #     return context


class ArticlesView(ListView):
    template_name = 'articles/articles_page.html'
    model = Articles

    def get_queryset(self):
        return Articles.objects.all().order_by('-date')[:20]

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['articles'] = Articles.objects.all()
    #     return context


class CreateArticleView(CreateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'articles/article_create_page.html'

    def get_success_url(self):
        return reverse('articles')

    def get_initial(self):
        initial = {
            'date': now()
        }
        return initial

