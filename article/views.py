from django.core.exceptions import FieldError, EmptyResultSet
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import ArticleSection, Article
from forum.models import Topic
from mtf_hackathon import settings


class ArticleList(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try :

            search = request.GET.get("search")


            article = ArticleSection.objects.all()
            if not search :
                category = request.GET.get("category")
                if not category:
                    raise FieldError("category or search input not valid")
                categoryObject = Topic.objects.get(topic=category)
                if not categoryObject:
                    raise EmptyResultSet

                article = ArticleSection.objects.filter(topic=categoryObject)

                articleSection = []
                for i in article :
                    article = []
                    for j in i.section.all() :
                        article.append({
                            "id" : j.id,
                            "title" : j.title,
                            "content" : j.content
                        })
                    articleSection.append({
                        "id" : i.id,
                        "title" : i.title,
                        "article" : article
                    })

                return Response({
                    "status" : status.HTTP_200_OK,
                    "message" : "success",
                    "data" : {
                        'section' : articleSection,
                        'count' : len(articleSection),
                    }
                }, status=status.HTTP_200_OK)

            else :
                article = Article.objects.filter(title__icontains=search)
                articles = []
                for i in article :
                    articles.append({
                        'id' : i.id,
                        'title' : i.title,
                        'content' : i.content
                    })

                return Response({
                    "status": status.HTTP_200_OK,
                    "message": "success",
                    "data": {
                        "articles" : articles,
                        'count': len(article)
                    }
                }, status=status.HTTP_200_OK)


        except FieldError as e:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "paramater invalid",
                "data": repr(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        except EmptyResultSet as e :
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": "category not found",
                "data": repr(e)
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            if settings.DEBUG:
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "internal server error",
                    "data": repr(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else :
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "internal server error"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ArticleDetail(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try :
            article = Article.objects.filter(id=id)
            if id == "":
                raise FieldError("id input not valid")
            if not article:
                raise EmptyResultSet("no result for forum id = " + str(id))
            else:
                article = Article.objects.get(id=id)

            return Response({
                "status" : status.HTTP_200_OK,
                "message" : "success",
                "data" : {
                    "id" : article.id,
                    "title" : article.title,
                    "content" : article.content
                }
            }, status=status.HTTP_200_OK)

        except FieldError as e:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "paramater invalid",
                "data": repr(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        except EmptyResultSet as e :
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": "category not found",
                "data": repr(e)
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            if settings.DEBUG:
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "internal server error",
                    "data": repr(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else :
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "internal server error"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
