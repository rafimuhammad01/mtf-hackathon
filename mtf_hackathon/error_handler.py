from rest_framework import status
from rest_framework.response import Response

from mtf_hackathon import settings


def PermissionDeniedHandler(e) :
    return Response({
        "status": status.HTTP_401_UNAUTHORIZED,
        "message": "unauthorized",
        "data": repr(e)
    }, status=status.HTTP_401_UNAUTHORIZED)

def FieldErrorHandler(e) :
    return Response({
        "status": status.HTTP_400_BAD_REQUEST,
        "message": "paramater invalid",
        "data": repr(e)
    }, status=status.HTTP_400_BAD_REQUEST)

def EmptyResultSetHandler(e) :
    return Response({
        "status": status.HTTP_404_NOT_FOUND,
        "message": "not found",
        "data": repr(e)
    }, status=status.HTTP_404_NOT_FOUND)

def ExceptionHandler(e) :
    if settings.DEBUG:
        return Response({
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "internal server error",
            "data": repr(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "internal server error"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)