from django.core.exceptions import FieldError, EmptyResultSet
from django.db.models import Count
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from JWTAuth.models import Employee
from mtf_hackathon import settings
from .models import Forum, Topic, Answer


# Create your views here.
class ForumList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            category = request.GET.get("category")
            sortInput = request.GET.get("sort")
            search = request.GET.get("search")

            forum = Forum.objects.all()

            # Validate search
            if not search :
                # Validate category and sort
                if category == "":
                    raise FieldError("category input not valid")
                if sortInput == "":
                    raise FieldError("sort input not valid")
    
                # Get topic object based on category
                categoryObject = Topic.objects.get(topic=category)
                if not categoryObject:
                    raise EmptyResultSet
    
                # Get forum based on category and sort input
                if sortInput == "date":
                    forum = Forum.objects.filter(topic__in=[categoryObject.id]).order_by("-createdAt")
                elif sortInput == "vote":
                    forum = Forum.objects.filter(topic__in=[categoryObject.id]).annotate(num_vote=Count('upvote')).order_by(
                        '-num_vote')
                elif sortInput == "answer":
                    forum = Forum.objects.filter(topic__in=[categoryObject.id]).annotate(
                        num_answer=Count('answer')).order_by('-num_answer')
                else:
                    raise FieldError("sort input not valid")
                
            else : # if sort exist
                forum = Forum.objects.filter(title__contains=search)
        
            # Create list of forum
            forumList = []
            for i in forum:

                # Check is upvote
                isUpvote = False
                if Employee.objects.get(user=request.user) in i.upvote.all():
                    isUpvote = True

                # Append
                forumList.append(
                    {
                        "id": i.id,
                        "username": i.owner.user.username,
                        "title": i.title,
                        "question": i.question,
                        "upvote": i.upvote.count(),
                        "total_answer": i.answer.count(),
                        "created_at": i.createdAt,
                        "is_upvote": isUpvote
                    }
                )

            # Response
            resp = {
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": {
                    "forum": forumList,
                    "count": forum.count()
                }
            }

            return Response(resp, status=status.HTTP_200_OK)
            
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
            else:
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "internal server error"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try :
            if request.data['title'] == "" :
                raise FieldError("title is not valid")
            if request.data['question'] == "" :
                raise FieldError("question is not valid")
            if request.data['topic']  == "" :
                raise FieldError("topic is not valid")

            owner  = Employee.objects.get(user=request.user)
            forum = Forum.objects.create(title = request.data['title'], question =request.data['question'], owner=owner)

            for i in request.data['topic'] :
                topic = Topic.objects.filter(topic=i)
                if topic.count() == 0 :
                    topic = Topic.objects.create(topic=i)
                else :
                    topic = topic[0]

                forum.topic.add(topic)

            answer = []
            for i in forum.answer.all():
                isUpvote = False
                if Employee.objects.get(user=request.user) in i.upvote.all():
                    isUpvote = True
                data = {
                    "id": i.id,
                    "username": i.owner.user.username,
                    "answer": i.answer,
                    "upvote": i.upvote.count(),
                    "is_upvote": isUpvote
                }
                answer.append(data)

            isUpvote = False
            if Employee.objects.get(user=request.user) in forum.upvote.all():
                isUpvote = True

            return Response({
                "status" : status.HTTP_201_CREATED,
                "message" : "object created",
                "data" : {
                    "id" : forum.id,
                    "username" : forum.owner.user.username,
                    "title" : forum.title,
                    "question" : forum.question,
                    "upvote" : forum.upvote.count(),
                    "answer" : answer,
                    "is_upvote" : isUpvote,
                    "created_at" : forum.createdAt
                }
            })


        except FieldError as e:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "paramater invalid",
                "data": repr(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        except EmptyResultSet as e:
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
            else:
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "internal server error"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ForumDetail(APIView) :
    def get(self, request, id):
        try :
            forum = Forum.objects.filter(id=id)
            if id == "" :
                raise FieldError("id input not valid")
            if not forum:
                raise EmptyResultSet("no result for forum id = "+ str(id))
            else :
                forum = Forum.objects.get(id=id)


            answer = []
            for i in forum.answer.all() :
                isUpvote = False
                if Employee.objects.get(user=request.user) in i.upvote.all():
                    isUpvote = True
                data = {
                    "id" : i.id,
                    "username" : i.owner.user.username,
                    "answer" : i.answer,
                    "upvote" : i.upvote.count(),
                    "is_upvote" : isUpvote,
                    "created_at": i.createdAt
                }
                answer.append(data)
            isUpvote = False
            if Employee.objects.get(user=request.user) in forum.upvote.all():
                isUpvote = True

            return Response({
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": {
                    "id" : forum.id,
                    "username" : forum.owner.user.username,
                    "title" : forum.title,
                    "question" : forum.question,
                    "upvote" : forum.upvote.count(),
                    "answer" : answer,
                    "is_upvote" : isUpvote,
                    "created_at" : forum.createdAt
                }
            })

        
        except FieldError as e :
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
            else:
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "internal server error"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, id):
        try :
            forum = Forum.objects.get(id=id)
            if id == "":
                raise FieldError("id input not valid")
            if forum == []:
                raise EmptyResultSet("no result for forum id = ", id)
            if request.data['answer'] == "" :
                raise FieldError("answer is not valid")

            owner = Employee.objects.get(user=request.user)
            answer = Answer.objects.create(answer=request.data['answer'], owner=owner)
            forum.answer.add(answer)

            isUpvote = False
            if Employee.objects.get(user=request.user) in answer.upvote.all():
                isUpvote = True

            return Response({
                "status" : status.HTTP_201_CREATED,
                "message" : "objects created",
                "data" : {
                    "id" : answer.id,
                    "username" : answer.owner.user.username,
                    "upvote" : answer.upvote.count(),
                    "is_upvote" : isUpvote,
                    "created_at" : answer.createdAt
                }
            })


        except FieldError as e :
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
            else:
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "internal server error"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VoteForumIncrement(APIView) :
    permission_classes = [IsAuthenticated]

    def post (self, request, id) :
        try :
            forum = Forum.objects.get(id=id)
            if id == "":
                raise FieldError("id input not valid")
            if forum == []:
                raise EmptyResultSet("no result for forum id = ", id)
            if request.data['is_increase'] == "":
                raise FieldError("answer is not valid")

            employee = Employee.objects.get(user=request.user)
            if request.data['is_increase'] == "true" :
                if employee in forum.upvote.all():
                    raise Exception("Already upvote")
                else :
                    forum.upvote.add(employee)
            else :
                forum.upvote.remove(employee)

            isUpvote = False
            if Employee.objects.get(user=request.user) in forum.upvote.all():
                isUpvote = True

            return Response({
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": {
                    "id": forum.id,
                    "username": forum.owner.user.username,
                    "title": forum.title,
                    "question": forum.question,
                    "upvote": forum.upvote.count(),
                    "is_upvote": isUpvote,
                    "created_at": forum.createdAt
                }
            })

        except FieldError as e :
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
            else:
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "internal server error"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VoteAnswerIncrement(APIView) :
    permission_classes = [IsAuthenticated]

    def post (self, request, id) :
        try :
            answer = Answer.objects.get(id=id)
            if id == "":
                raise FieldError("id input not valid")
            if answer == []:
                raise EmptyResultSet("no result for forum id = ", id)
            if request.data['is_increase'] == "":
                raise FieldError("answer is not valid")

            employee = Employee.objects.get(user=request.user)
            if request.data['is_increase'] == "true" :
                if employee in answer.upvote.all():
                    raise Exception("Already upvote")
                else :
                    answer.upvote.add(employee)
            else :
                answer.upvote.remove(employee)

            isUpvote = False
            if Employee.objects.get(user=request.user) in answer.upvote.all():
                isUpvote = True

            return Response({
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": {
                    "id": answer.id,
                    "username": answer.owner.user.username,
                    "upvote": answer.upvote.count(),
                    "is_upvote": isUpvote,
                    "created_at": answer.createdAt
                }
            })

        except FieldError as e :
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
            else:
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "internal server error"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)