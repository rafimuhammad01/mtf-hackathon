import base64

from django.core.exceptions import EmptyResultSet
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from JWTAuth.models import Employee
# Create your views here.
from course.models import CourseOwned, Course
from mtf_hackathon.error_handler import EmptyResultSetHandler, ExceptionHandler


class CourseList(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            employee = Employee.objects.filter(user=request.user)
            if not employee :
                raise EmptyResultSet("Employee not found")
            else :
                employee = employee[0]

            myCourse = CourseOwned.objects.filter(owner=employee)
            myCourseResponse = []

            for i in myCourse :
                data = {
                    "id" : i.course.id,
                    "name" : i.course.name,
                    "topic" : [j.topic for j in i.course.topic.all()] ,
                    "last_lesson" : {
                        "id" : i.lastLesson.id,
                        "title" : i.lastLesson.title
                    },
                    "progress" : i.progress,
                    "img" : i.course.img.url
                }
                myCourseResponse.append(data)

            recomendation = []
            userCourse = CourseOwned.objects.filter(owner=employee)
            if not userCourse :
                allCourse = Course.objects.all()
                for i in allCourse :
                    recomendation.append({
                        "id" : i.id,
                        "name" : i.name,
                        "description" : i.description,
                        "topic" : [j.topic for j in i.topic.all()],
                        "img" : i.img.url,
                        "price" : i.price,
                        "reward" : i.reward
                    })


            else :
                userCourseList = []
                for i in userCourse :
                    userCourseList.append(i.course)
                topicID = []
                for i in userCourse :
                    for j in i.course.topic.all() :
                        topicID.append(j.id)

                filteredCourse = Course.objects.filter(topic__in=topicID, )
                for i in filteredCourse :
                    if i not in userCourseList :
                        recomendation.append({
                            "id" : i.id,
                            "name" : i.name,
                            "description" : i.description,
                            "topic" : [j.topic for j in i.topic.all()],
                            "img" : i.img.url,
                            "price" : i.price,
                            "reward" : i.reward
                        })

            response = {
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": {
                    "my_course" : myCourseResponse,
                    "recommendation" : recomendation
                }
            }

            return Response(response, status=status.HTTP_200_OK)


        except EmptyResultSet as e:
            return EmptyResultSetHandler(e)

