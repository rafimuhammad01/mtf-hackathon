from django.urls import include, path
from dashboard.views import DashboardView


urlpatterns = [
    path('', DashboardView.as_view()),
]