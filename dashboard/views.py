from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from JWTAuth.models import Employee
from adminpage.views import getAvg
from course.models import CourseOwned, StepOwned, QuizSectionOwned
from dashboard.models import BalanceHistory, Notification
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
        totalScore = 0
        countScore = 0
        for i in getAvg(employee) :
            if i["isWorkingOn"] :
                totalScore += i["score"]
                countScore += 1

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
                "avg_score" : totalScore/countScore,
                "pewira_miles_balance" : pewiraMilesBalance,
                "last_course" : lastCourse,
                "training" : training
            }
        })



class HistoryBalance(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee = Employee.objects.get(user=request.user)
        history = BalanceHistory.objects.filter(owner=employee)

        data = []
        for i in history :
            data.append({
                "id" : i.id,
                "balance" : i.balance,
                "type" : i.type,
                "description" : i.description,
                "date" : i.date
            })

        return Response({
            "status" : 200,
            "message" : "success",
            "data" : data
        }, status=status.HTTP_200_OK)


class ProfileView(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee = Employee.objects.get(user=request.user)

        return Response({
            "status" : 200,
            "message" : "success",
            "data" : {
                "id" : employee.user.id,
                "img" : employee.img.url,
                "first_name" : employee.user.first_name,
                "last_name" : employee.user.last_name,
                "sex" : employee.sex,
                "position" : employee.posistion,
                "department" : employee.department,
                "start_work_date" : employee.start_work_date,
            }
        })

    def put(self, request):
        employee = Employee.objects.get(user=request.user)
        employee.user.first_name = request.data["first_name"]
        employee.user.last_name = request.data["last_name"]
        employee.img = request.data["img"]
        employee.sex = request.data["sex"]
        employee.posistion = request.data['position']
        employee.department = request.data['department']
        employee.user.save()
        employee.save()
        newEmployee = Employee.objects.get(user=request.user)

        return Response({
            "status" : 201,
            "message" : "update success",
            "data" : {
                "id" : newEmployee.user.id,
                "img" : newEmployee.img.url,
                "first_name" : newEmployee.user.first_name,
                "last_name" : newEmployee.user.last_name,
                "sex" : newEmployee.sex,
                "position" : newEmployee.posistion,
                "department" : newEmployee.department,
                "start_work_date" : newEmployee.start_work_date,
            }
        })


class NotificationView(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request) :
        employee = Employee.objects.get(user=request.user)
        notification = Notification.objects.filter(owner=employee)

        dataResp = []
        for i in notification :
            dataResp.append({
                "id" : i.id,
                "created_at" : i.createdAt,
                "notif" : i.notif,
                "category" : i.category,
                "is_read" : i.isRead
            })

        return Response({
            "status" : 200,
            "message" : "success",
            "data" : dataResp
        })

    def post(self, request):
        employee = Employee.objects.get(user=request.user)
        notification = Notification.objects.filter(owner=employee)

        dataResp = []
        for i in notification:
            i.isRead = True
            dataResp.append({
                "id": i.id,
                "created_at": i.created_at,
                "notif": i.notif,
                "category": i.category,
                "is_read": i.isRead
            })
        return Response({
            "status": 201,
            "message": "status updated",
            "data": dataResp
        })