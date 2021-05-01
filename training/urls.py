from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from training.views import TrainingList, TrainingDetail

urlpatterns = [
    path('', TrainingList.as_view()),
    path('<int:id>/', TrainingDetail.as_view())
]