from django.urls import include, path
from dashboard.views import DashboardView, HistoryBalance, ProfileView, NotificationView

urlpatterns = [
    path('', DashboardView.as_view()),
    path('history/', HistoryBalance.as_view()),
    path('profile/', ProfileView.as_view()),
    path('notification/', NotificationView.as_view())
]