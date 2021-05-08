from django.urls import path

from adminpage.views import DashboardView, CourseView, TrainingView, EmployeeView, EmployeeDetailView, \
    PewiraMilesBalanceView

urlpatterns = [
    path('dashboard/', DashboardView.as_view()),
    path('course/', CourseView.as_view()),
    path('training/', TrainingView.as_view()),
    path('employee/', EmployeeView.as_view()),
    path('employee/<str:username>', EmployeeDetailView.as_view()),
    path('pewiraMiles/', PewiraMilesBalanceView.as_view()),
]