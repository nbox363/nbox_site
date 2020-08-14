from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.utils.timezone import now
from django.contrib.auth.models import User

from .forms import ArticlesForm, AddCommentForm
from .models import Articles, Comments, Category


class ArticleView(DetailView):
    template_name = 'articles/article_page.html'
    model = Articles

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class ArticlesView(ListView):
    template_name = 'articles/articles_page.html'
    model = Articles

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Articles.objects.all().order_by('-date')[:20]
        context['categories'] = Category.objects.all()
        return context


class CreateArticleView(CreateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'articles/article_create_page.html'
    initial = {'date': now()}
    success_url = reverse_lazy('articles')


class AddCommentView(CreateView):
    model = Comments
    form_class = AddCommentForm
    initial = {'author': User}
    template_name = 'articles/add_comment.html'
    success_url = reverse_lazy('articles')


def current_category_view(request, category_name):
    category_article = Articles.objects.filter(category=category_name)
    context = {'category_name':    category_name,
               'category_article': category_article}
    template = 'articles/by_category_view.html'
    return render(request, template, context)


class AllCategoryView(ListView):
    template_name = 'articles/all_category_view.html'
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context







