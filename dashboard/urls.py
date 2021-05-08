from django.urls import include, path
from dashboard.views import DashboardView, HistoryBalance, ProfileView

urlpatterns = [
    path('', DashboardView.as_view()),
    path('history/', HistoryBalance.as_view()),
    path('profile/', ProfileView.as_view())
]