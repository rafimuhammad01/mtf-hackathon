import base64
from datetime import datetime

from django.db.models import Q
from django.core.exceptions import EmptyResultSet, FieldError
from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from JWTAuth.models import Employee
# Create your views here.
from course.models import CourseOwned, Course, LessonOwned, StepOwned, SectionOwned, QuizOwned, Lesson, Step, Quiz, \
    Choice, QuizSectionOwned, QuizSection
from forum.models import Forum, Topic
from mtf_hackathon.error_handler import EmptyResultSetHandler, ExceptionHandler, FieldErrorHandler, \
    PermissionDeniedHandler


class CourseList(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            employee = Employee.objects.filter(user=request.user)
            search = request.GET.get("search")
            if not employee :
                raise EmptyResultSet("Employee not found")
            else :
                employee = employee[0]

            myCourse = CourseOwned.objects.all()
            myCourseResponse = []

            if search :
                topicID = []
                for i in Topic.objects.filter(topic__icontains=search):
                    topicID.append(i.id)

                courseID = []
                for i in Course.objects.filter(Q(name__icontains=search) | Q(topic__in=topicID)) :
                    courseID.append(i.id)

                myCourse = CourseOwned.objects.filter(Q(owner=employee) & Q(course__in=courseID))

            else :
                myCourse = CourseOwned.objects.filter(owner=employee)
            lst = []
            for i in myCourse :
                data = {}
                if i.lastLesson :
                    data = {
                        "id" : i.course.id,
                        "name" : i.course.name,
                        "topic" : [j.topic for j in i.course.topic.all()] ,
                        "last_progress" : {
                            "id" : i.lastLesson.id,
                            "title" : i.lastLesson.title,
                            "type" : "lesson",
                            "step" : {
                                "id" : i.lastStep.id,
                                "title" : i.lastStep.title
                            }
                        },
                        "progress" : i.totalComplete / i.course.totalStepAndQuiz if i.course.totalStepAndQuiz != 0 else 0.0 ,
                        "img" : i.course.img.url
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
                        "progress": i.totalComplete / i.course.totalStepAndQuiz if i.course.totalStepAndQuiz != 0 else 0.0 ,
                        "img": i.course.img.url
                    }
                else :
                    data = {
                        "id": i.course.id,
                        "name": i.course.name,
                        "topic": [j.topic for j in i.course.topic.all()],
                        "last_progress": {},
                        "progress": i.totalComplete / i.course.totalStepAndQuiz if i.course.totalStepAndQuiz != 0 else 0.0 ,
                        "img": i.course.img.url
                    }
                lst.append(data)
            myCourseResponse = {
                "list" : lst,
                "count" : len(lst)
            }


            courseResponse = {}
            course = []
            userCourse = CourseOwned.objects.filter(owner=employee)
            userCourseList = []
            for i in userCourse:
                userCourseList.append(i.course)
            if not search :
                if not userCourse :
                    allCourse = Course.objects.all()
                    for i in allCourse :
                        course.append({
                            "id" : i.id,
                            "name" : i.name,
                            "description" : i.description,
                            "topic" : [j.topic for j in i.topic.all()],
                            "img" : i.img.url,
                            "price" : i.price,
                            "reward" : i.reward
                        })


                else :
                    topicID = []
                    for i in userCourse :
                        for j in i.course.topic.all() :
                            topicID.append(j.id)

                    filteredCourse = Course.objects.filter(topic__in=topicID, )
                    for i in filteredCourse :
                        if i not in userCourseList :
                            course.append({
                                "id" : i.id,
                                "name" : i.name,
                                "description" : i.description,
                                "topic" : [j.topic for j in i.topic.all()],
                                "img" : i.img.url,
                                "price" : i.price,
                                "reward" : i.reward
                            })

            else :
                topicID = []
                for i in Topic.objects.filter(topic__icontains=search):
                    topicID.append(i.id)
                filteredCourse = Course.objects.filter(Q(name__icontains=search) | Q(topic__in=topicID)).distinct()
                for i in filteredCourse:
                    if i not in userCourseList:
                        course.append({
                            "id": i.id,
                            "name": i.name,
                            "description": i.description,
                            "topic": [j.topic for j in i.topic.all()],
                            "img": i.img.url,
                            "price": i.price,
                            "reward": i.reward
                        })

            courseResponse = {
                "list" : course,
                "count" : len(course)
            }
            response = {
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": {
                    "my_course" : myCourseResponse,
                    "course" : courseResponse
                }
            }

            return Response(response, status=status.HTTP_200_OK)


        except EmptyResultSet as e:
            return EmptyResultSetHandler(e)


class CourseDetail(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        employee = Employee.objects.get(user=request.user)
        course = Course.objects.get(id=id)
        data = {}
        courseOwned = CourseOwned.objects.filter(owner=employee, course=course)
        if not courseOwned :
            topic = [i.topic for i in course.topic.all()]
            section = []
            for i in course.section.all() :
                lesson = []
                quizSection = {
                    "id" : i.quizSection.id,
                    "title" : i.quizSection.title,
                    "description" : i.quizSection.title,
                    "quiz" : []
                }
                for j in i.lesson.all() :
                    lesson.append({
                        "id" : j.id,
                        "title" : j.title
                    })


                for j in  i.quizSection.quiz.all() :
                    quizSection["quiz"].append({
                        "id" : j.id,
                    })

                section.append({
                    "title" : i.title,
                    "lesson" : lesson,
                    "quiz_section" : quizSection
                })

            data = {
                "id" : course.id,
                "is_owned" : False,
                "name" : course.name,
                "about" : course.about,
                "learning_point" : course.learningPoint,
                "rating" : course.rating,
                "total_rating" : len(course.totalRating.all()),
                "total_participant" : course.totalParticipant,
                "estimate_time" : course.estimateTime,
                "img" : course.img.url,
                "price" : course.price,
                "topic" : topic,
                "section" : section,
            }
        else :
            courseOwned = CourseOwned.objects.filter(owner=employee, course=course)[0]
            section = []
            totalScore = 0
            quizCount = 0
            for i in course.section.all() :
                lesson = []
                quizSection = {
                    "id": i.quizSection.id,
                    "title": i.quizSection.title,
                    "description": i.quizSection.title,
                    "quiz": []
                }
                for j in i.lesson.all() :
                    lesson.append({
                        "id" : j.id,
                        "title" : j.title
                    })

                quizSectionOwned = QuizSectionOwned.objects.get(owner=employee, quizSection=i.quizSection)
                totalScore += quizSectionOwned.quizResult
                quizCount += 1
                for j in i.quizSection.quiz.all():
                    quizSection["quiz"].append({
                        "id": j.id,
                    })

                section.append({
                    "id" : i.id,
                    "title": i.title,
                    "lesson" : lesson,
                    "quiz_section" : quizSection
                })

            data = {
                "id": course.id,
                "is_owned": True,
                "name": course.name,
                "about": course.about,
                "learning_point": course.learningPoint,
                "section" : section,
                "total_score" : totalScore/quizCount
            }

            if courseOwned.lastLesson :
                lastCourse = {
                    "id" : courseOwned.lastLesson.id,
                    "name" : courseOwned.lastLesson.title,
                    "type" : "lesson",
                    "step" : {
                        "id" : courseOwned.lastStep.id,
                        "title" : courseOwned.lastStep.title
                    }
                }
                data['last_progress'] = lastCourse
            elif courseOwned.lastQuiz :
                lastQuiz = {
                    "id" : courseOwned.lastQuiz.id,
                    "name": courseOwned.lastQuiz.title,
                    "type": "quiz",
                }
                data['last_progress'] = lastQuiz
            else :
                data['last_progress'] = {}


        return Response({
            "status" : status.HTTP_200_OK,
            "message" : "success",
            "data" : data
        }, status=status.HTTP_200_OK)

    def post(self, request, id):
        employee = Employee.objects.get(user=request.user)
        course = Course.objects.get(id=id)

        courseOwned = CourseOwned.objects.filter(owner=employee, course=course)
        if not courseOwned:
            if employee.pewiraMilesBalance < course.price :
                return Response({
                    "status": status.HTTP_204_NO_CONTENT,
                    "message": "not enough pewira miles balance",
                }, status=status.HTTP_204_NO_CONTENT)
            else :
                newCourseOwned = CourseOwned.objects.create(owner=employee, course=course)
                for i in course.section.all() :
                    newSectionOwned = SectionOwned.objects.create(owner=employee, section=i)
                    newCourseOwned.sectionOwned.add(newSectionOwned)
                    for j in i.lesson.all() :
                        newLessonOwned = LessonOwned.objects.create(owner=employee, lesson=j)
                        newSectionOwned.lessonOwned.add(newLessonOwned)
                        for k in j.step.all() :
                            newStepOwned = StepOwned.objects.create(owner=employee, step=k)
                            newLessonOwned.stepOwned.add(newStepOwned)

                    newQuizSectionOwned = QuizSectionOwned.objects.create(owner=employee, quizSection=i.quizSection)
                    newSectionOwned.quizSectionOwned.add(newQuizSectionOwned)
                    for j in i.quizSection.quiz.all() :
                        newQuizOwned = QuizOwned.objects.create(owner=employee, quiz=j)
                        newQuizSectionOwned.quizOwned.add(newQuizOwned)

                employee.pewiraMilesBalance -= course.price
                employee.save()
                course.totalParticipant += 1
                course.save()
                return Response({
                    "status": status.HTTP_201_CREATED,
                    "message": "success",
                }, status=status.HTTP_201_CREATED)
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "already have courses",
        }, status=status.HTTP_400_BAD_REQUEST)



class LessonView(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:
            employee = Employee.objects.get(user=request.user)
            lessonOwned = LessonOwned.objects.filter(lesson__id=id, owner=employee)
            print(employee)
            print(lessonOwned)
            if not lessonOwned :
                raise PermissionDenied("user do not have this lesson")
            else :
                lessonOwned = LessonOwned.objects.filter(lesson__id=id, owner=employee)[0]

            dataResponse = []
            for i in lessonOwned.stepOwned.all() :
                data = {
                    "id" : i.step.id,
                    "title" : i.step.title,
                    "type" : i.step.type,
                    "is_complete" : i.isComplete,
                }
                dataResponse.append(data)

            return Response({
                "status" : status.HTTP_200_OK,
                "message" : "success",
                "data" :
                    {
                        "steps" : dataResponse
                    }
            })
        except PermissionDenied as e :
            return PermissionDeniedHandler(e)

        except Exception as e :
            return ExceptionHandler(e)

    def post(self, request, id):
        try:
            employee = Employee.objects.get(user=request.user)
            lessonOwned = LessonOwned.objects.get(lesson__id=id, owner=employee)

            if not lessonOwned.isComplete :
                isComplete = False
                for i in lessonOwned.stepOwned.all() :
                    if not i.isComplete :
                        isComplete = False
                        break
                    else :
                        isComplete = True

                lessonOwned.isComplete = isComplete
                lessonOwned.save()



            return Response({
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": {
                    "id" : lessonOwned.lesson.id,
                    "is_complete" : lessonOwned.isComplete
                }

            })

        except FieldError as e:
            return FieldErrorHandler(e)

        except Exception as e :
            return ExceptionHandler(e)

class StepView(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request, id):

        try :
            employee = Employee.objects.get(user=request.user)
            stepOwned = StepOwned.objects.get(step__id=id, owner=employee)


            data = {
                "id": stepOwned.step.id,
                "title": stepOwned.step.title,
                "type": stepOwned.step.type,
                "content_text": stepOwned.step.contentText,
                "content_video": stepOwned.step.contentVideo,
                "transcript": stepOwned.step.transcript,
                "is_complete": stepOwned.isComplete,
                "time_consume": stepOwned.timeConsume if stepOwned.timeConsume else '00:00:00',
                "next_id" : stepOwned.step.nextID.id if stepOwned.step.nextID else -1,
                "prev_id": stepOwned.step.prevID.id if stepOwned.step.prevID else -1,
            }

            return Response({
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": data
            })
        except Exception as e :
            return ExceptionHandler(e)

    def post(self, request, id):
        try:
            timestamp = request.data['timestamp']

            if not timestamp:
                raise FieldError("timestamp is not valid")

            employee = Employee.objects.get(user=request.user)
            step = Step.objects.get(id=id)
            print(step)
            stepOwned = StepOwned.objects.get(step__id=id, owner=employee)

            if not stepOwned.isComplete :
                stepOwned.isComplete = True if datetime.strptime(timestamp, '%H:%M:%S').time() >= stepOwned.step.timeMinimum else False
                stepOwned.timeConsume = timestamp
                stepOwned.save()

                if stepOwned.isComplete :
                    lessonOwned = LessonOwned.objects.filter(stepOwned=stepOwned)[0]
                    sectionOwned = SectionOwned.objects.filter(lessonOwned=lessonOwned)[0]
                    courseOwned = CourseOwned.objects.filter(sectionOwned=sectionOwned)[0]

                    courseOwned.lastLesson = lessonOwned.lesson
                    courseOwned.lastStep = stepOwned.step
                    courseOwned.lastQuiz = None
                    courseOwned.totalComplete += 1
                    courseOwned.save()





            return Response({
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": {
                    "id" : stepOwned.step.id,
                    "time_consume" : stepOwned.timeConsume,
                    "is_complete" : stepOwned.isComplete
                }

            })

        except FieldError as e:
            return FieldErrorHandler(e)

        except Exception as e :
            return ExceptionHandler(e)


class QuizView(APIView) :
    def get(self, request, id):

        try :
            dataRes = {}
            allQuiz = []
            owner = Employee.objects.get(user=request.user)
            for i in QuizSectionOwned.objects.get(quizSection_id=id, owner=owner).quizOwned.all():
                data = {
                    "id": i.quiz.id,
                    "question": i.quiz.question,
                    "choice_1": {
                        "id": i.quiz.choice1.id,
                        "choice": i.quiz.choice1.choice,
                        "is_right": i.quiz.choice1.isRight
                    },
                    "choice_2": {
                        "id": i.quiz.choice2.id,
                        "choice": i.quiz.choice2.choice,
                        "is_right": i.quiz.choice2.isRight
                    },
                    "choice_3": {
                        "id": i.quiz.choice3.id,
                        "choice": i.quiz.choice3.choice,
                        "is_right": i.quiz.choice3.isRight
                    },
                    "choice_4": {
                        "id": i.quiz.choice4.id,
                        "choice": i.quiz.choice4.choice,
                        "is_right": i.quiz.choice4.isRight
                    },
                    "point": i.quiz.point
                }
                allQuiz.append(data)

            dataRes["quiz_section"] = allQuiz
            dataRes["attempt"] = QuizSectionOwned.objects.get(quizSection_id=id, owner=owner).attempt
            return Response({
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": dataRes
            })
        except Exception as e:
            return ExceptionHandler(e)

    def post(self, request, id):
        try:
            '''
            answer : [
                {
                    id :
                    question :
                    answer : {
                        id : 
                        answer : 
                    }
                },
                {
                    id :
                    question :
                    answer : {
                        id : 
                        answer : 
                    }
                },
                
            ]
            '''


            employee = Employee.objects.get(user=request.user)
            totalPoint = 0

            quizSection = QuizSection.objects.get(id=id)
            quizSectionOwned = QuizSectionOwned.objects.get(owner=employee, quizSection_id=id)

            if quizSectionOwned.attempt < 3 :
                allPoint = 0
                for i in request.data["answer"] :
                    quizOwned = QuizOwned.objects.get(owner = employee, quiz_id=i["id"])
                    answer = Choice.objects.get(id=i["answer"]["id"])
                    quizOwned.isRight = answer.isRight
                    quizOwned.save()
                    if quizOwned.isRight :
                        totalPoint += quizOwned.quiz.point
                    allPoint += quizOwned.quiz.point

                quizSectionOwned.quizResult = (totalPoint / allPoint) * 100
                quizSectionOwned.attempt += 1
                quizSectionOwned.save()
                if quizSectionOwned.quizResult >= quizSection.minimumQuizScore :
                    quizSectionOwned.isPassedQuiz = True
                    quizSectionOwned.isComplete = True
                    quizSectionOwned.save()

                    sectionOwned = SectionOwned.objects.filter(quizSectionOwned=quizSectionOwned)[0]
                    courseOwned = CourseOwned.objects.filter(sectionOwned=sectionOwned)[0]

                    courseOwned.lastLesson = None
                    courseOwned.lastStep = None
                    courseOwned.lastQuiz = quizSection
                    courseOwned.totalComplete += 1
                    courseOwned.save()
            else :
                raise PermissionDenied("maximum attempt")


            return Response({
                "status" : status.HTTP_200_OK,
                "message" : "success",
                "data" : {
                    "id" : quizSection.id,
                    "is_complete" : quizSectionOwned.isComplete,
                    "quiz_result" : quizSectionOwned.quizResult,
                    "is_passed" : quizSectionOwned.isPassedQuiz,
                    "attempt" : quizSectionOwned.attempt
                }
            }, status=status.HTTP_200_OK)


        except PermissionDenied as e :
            return PermissionDeniedHandler(e)

        except AttributeError as e:
            return FieldErrorHandler(e)

        except Exception as e:
            return ExceptionHandler(e)
