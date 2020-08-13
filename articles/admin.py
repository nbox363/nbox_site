from django.contrib import admin

from articles.models import Articles, Comments, Category

admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(Category)
