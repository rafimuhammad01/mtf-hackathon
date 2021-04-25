from django.contrib import admin
from django.urls import include, path

from article.views import ArticleList, ArticleDetail

urlpatterns = [
    path('', ArticleList.as_view()),
    path('<int:id>', ArticleDetail.as_view())
]