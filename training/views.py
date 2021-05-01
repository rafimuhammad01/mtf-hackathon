from datetime import datetime

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from mtf_hackathon.error_handler import EmptyResultSetHandler, ExceptionHandler, FieldErrorHandler, \
    PermissionDeniedHandler
from JWTAuth.models import Employee
from training.models import TrainingOwned, Schedule


class  TrainingList(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            if not request.GET.get("date") :

                owner = Employee.objects.get(user=request.user)
                idTrainingOwned = [i.training.id for i in TrainingOwned.objects.filter(owner=owner)]

                schedule = Schedule.objects.filter(training__in=idTrainingOwned).order_by("startTime")


                dicts = {}
                for i in schedule :
                    if i.startTime.date() in dicts :
                        data = {
                            "id" : i.id,
                            "name" : i.training.name,
                            "img" : i.training.img.url,
                            "start_time" : i.startTime,
                            "end_time" : i.endTime
                        }
                        if i.method == 0:
                            data["linkUrl"] = i.linkUrl
                        elif i.method == 1:
                            data['location'] = i.location
                        dicts[i.startTime.date()].append(data)
                    else :
                        lst = []
                        data = {
                            "id": i.id,
                            "name": i.training.name,
                            "img": i.training.img.url,
                            "start_time": i.startTime,
                            "end_time": i.endTime
                        }
                        if i.method == 0:
                            data["linkUrl"] = i.linkUrl
                        elif i.method == 1:
                            data['location'] = i.location
                        lst.append(data)
                        dicts[i.startTime.date()] = lst

                dataresp = []
                for x,y in dicts.items() :
                    dataresp.append(
                        {

                            "date" : x,
                            "training" : y
                        }
                    )

            else :

                dataresp = []
                owner = Employee.objects.get(user=request.user)
                idTrainingOwned = [i.training.id for i in TrainingOwned.objects.filter(owner=owner)]
                dateInput = request.GET.get("date")
                date = datetime.strptime(dateInput, "%Y-%m-%d").date()

                schedule = Schedule.objects.filter(training__in=idTrainingOwned, startTime__date=date)

                for i in schedule :
                    data = {
                        "id": i.id,
                        "name": i.training.name,
                        "img": i.training.img.url,
                        "method" : i.method,
                        "start_time": i.startTime,
                        "end_time": i.endTime,
                    }
                    if i.method == 0 :
                        data["linkUrl"] = i.linkUrl
                    elif i.method == 1 :
                        data['location'] = i.location

                    dataresp.append(data)


            return Response({
                "status" : status.HTTP_200_OK,
                "message" : "success",
                "data" : dataresp
            })

            '''
            data : [
                {
                    date : ,
                    training :[
                        {
                            "id" :,
                            "name" : ,
                            "img" : ,
                            " "
                        }
                    ] ,
                },
                {
                    date : ,
                    training :[]
                }
            
            ]
            
            '''



        except Exception as e:
            return ExceptionHandler(e)



class TrainingDetail(APIView) :
    def get(self, request, id):
        employee = Employee.objects.get(user=request.user)
        schedule = Schedule.objects.get(id=id)
        training = TrainingOwned.objects.get(training=schedule.training, owner=employee)

        res = {
            "id" : schedule.id,
            "name" : training.training.name,
            "img" : training.training.img.url,
            "organizer" : training.training.organizer,
            "about" : training.training.about,
            "date" : schedule.startTime.date(),
            "start_time" : schedule.startTime.strftime("%H:%M:%S"),
            "end_time" : schedule.endTime.strftime("%H:%M:%S"),
            "method" : schedule.method
        }

        if schedule.method == 0 :
            res["linkUrl"] = schedule.linkUrl
        elif schedule.method == 1 :
            res["location"] = schedule.location

        return Response({
            "status" : status.HTTP_200_OK,
            "message" : "success",
            "data" : res
        })