from .models import Category


def add_categories_context_to_the_paga(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['categories'] = Category.objects.all()
    return context