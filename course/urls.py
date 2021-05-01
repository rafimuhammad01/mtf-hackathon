from django.urls import path

from course.views import CourseList, LessonView, StepView, CourseDetail, QuizView

urlpatterns = [
    path('', CourseList.as_view()),
    path('lesson/<int:id>/', LessonView.as_view()),
    path('step/<int:id>/', StepView.as_view()),
    path('<int:id>/', CourseDetail.as_view()),
    path('quiz/<int:id>/', QuizView.as_view())
]