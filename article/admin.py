from django.contrib import admin

# Register your models here.
from article.models import ArticleSection, Article

admin.site.register(ArticleSection)
admin.site.register(Article)