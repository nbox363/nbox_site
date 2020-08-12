from django.views.generic import DetailView, ListView, FormView
from django.shortcuts import render, reverse, redirect

from .forms import ArticlesForm
from .models import Articles, Comments


def article_create_view(request):
    form = ArticlesForm()
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            Articles.objects.create(**form.cleaned_data)
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
        context['comments'] = Comments.objects.all()
        return context


class ArticlesView(ListView):
    template_name = 'articles/articles_page.html'

    def get_queryset(self):
        return Articles.objects.all().order_by('-date')[:5]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Articles.objects.all()
        return context


# class ArticleCreateView(FormView):
#     template_name = 'articles/article_create_page.html'
#     form_class = ArticlesForm
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['article'] = Articles.objects.all()
#         return context
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#     def get_form(self, form_class=None):
#         self.objects = super().get_form(form_class)
#         return self.objects
#
#     def get_success_url(self):
#         return reverse('articles')
