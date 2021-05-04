from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from JWTAuth.models import Employee
from course.models import CourseOwned, StepOwned, QuizSectionOwned
from training.models import TrainingOwned
from training.views import TrainingList, TrainingListToJSON
from rest_framework.views import APIView


class DashboardView(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request) :
        employee = Employee.objects.get(user=request.user)
        courseOwned = CourseOwned.objects.filter(owner=employee)
        trainingOwned = TrainingOwned.objects.filter(owner=employee)
        courseTrainingTotal = courseOwned.count() + trainingOwned.count()

        totalSpentTime = 0
        for i in StepOwned.objects.filter(owner=employee):
            totalSpentTime = i.timeConsume

        pewiraMilesBalance = employee.pewiraMilesBalance

        quizSectionOwned = QuizSectionOwned.objects.filter(owner=employee)
        lst = [i.quizResult for i in quizSectionOwned]
        avgScore = sum(lst) / len(lst)

        lastCourse = []
        for i in courseOwned :
            data = {}
            if i.lastLesson :
                data = {
                    "id": i.course.id,
                    "name": i.course.name,
                    "topic": [j.topic for j in i.course.topic.all()],
                    "last_progress": {
                        "id": i.lastLesson.id,
                        "title": i.lastLesson.title,
                        "type": "lesson",
                        "step": {
                            "id": i.lastStep.id,
                            "title": i.lastStep.title
                        }
                    },
                    "progress": i.totalComplete / i.course.totalStepAndQuiz if i.course.totalStepAndQuiz != 0 else 0.0,
                    "img": i.course.img.url
                }

            elif i.lastQuiz:
                data = {
                    "id": i.course.id,
                    "name": i.course.name,
                    "topic": [j.topic for j in i.course.topic.all()],
                    "last_progress": {
                        "id": i.lastQuiz.id,
                        "title": i.lastQuiz.title,
                        "type": "quiz"
                    },
                    "progress": i.totalComplete / i.course.totalStepAndQuiz if i.course.totalStepAndQuiz != 0 else 0.0,
                    "img": i.course.img.url
                }

            else:
                data = {
                    "id": i.course.id,
                    "name": i.course.name,
                    "topic": [j.topic for j in i.course.topic.all()],
                    "last_progress": {},
                    "progress": i.totalComplete / i.course.totalStepAndQuiz if i.course.totalStepAndQuiz != 0 else 0.0,
                    "img": i.course.img.url
                }
            lastCourse.append(data)


        training = TrainingListToJSON(request)
        return Response({
            "status" : status.HTTP_200_OK,
            "message" : "success",
            "data" : {
                "course_training_total" : courseTrainingTotal,
                "total_spent_time" : totalSpentTime,
                "avg_score" : avgScore,
                "pewira_miles_balance" : pewiraMilesBalance,
                "last_course" : lastCourse,
                "training" : training
            }
        })



