from django.urls import path

from course.views import CourseList
from forum.views import ForumDetail

urlpatterns = [
    path('', CourseList.as_view()),
]