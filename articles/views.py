from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.http import HttpResponseRedirect


from .forms import AddCommentForm
from .models import Articles, Comments, Category


class ArticleView(DetailView, CreateView):
    template_name = 'articles/article_page.html'
    model = Articles
    form_class = AddCommentForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('#redirect_after_post_a_comment')


class ArticlesView(ListView):
    template_name = 'articles/articles_page.html'
    model = Articles

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Articles.objects.all().order_by('-date')[:20]
        context['categories'] = Category.objects.all()
        return context


def current_category_view(request, category_name):
    category_article = Articles.objects.filter(category=category_name)
    context = {'category_name':    category_name,
               'category_article': category_article,
               'categories': Category.objects.all()}
    template = 'articles/by_category_view.html'
    return render(request, template, context)

