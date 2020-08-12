from django.contrib import admin

from articles.models import Articles, Comments

admin.site.register(Articles)
admin.site.register(Comments)
