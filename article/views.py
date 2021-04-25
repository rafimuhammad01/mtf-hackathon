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
from mtf_hackathon.error_handler import FieldErrorHandler, ExceptionHandler, EmptyResultSetHandler


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
            return FieldErrorHandler(e)

        except EmptyResultSet as e:
            return EmptyResultSetHandler(e)

        except Exception as e:
            return ExceptionHandler(e)


class ArticleDetail(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try :
            article = Article.objects.filter(id=id)
            if id == "":
                raise FieldError("id input not valid")
            if not article:
                raise EmptyResultSet("no result for article id = " + str(id))
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
            return FieldErrorHandler(e)

        except EmptyResultSet as e:
            return EmptyResultSetHandler(e)

        except Exception as e:
            return ExceptionHandler(e)
