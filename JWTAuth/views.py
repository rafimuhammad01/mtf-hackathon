from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee

from .serializers import RegisterSerializer, EmployeeSerializer


# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class EmployeeView (APIView) :
    permission_classes = [IsAuthenticated]
    def get (self, request) :
        employee = Employee.objects.get(user=request.user)
        resp = {
            "status" : 200,
            "message" : "",
            "data" : {
                "id" : employee.id,
                "username" : employee.user.username,
                "email" : employee.user.email,
                "status" : employee.status,
                "pewira_miles_balance" : employee.pewiraMilesBalance
            }
        }
        return Response(resp, status=status.HTTP_200_OK)