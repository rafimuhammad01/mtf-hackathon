from datetime import datetime

from django.db.models import Q
from django.utils import timezone
from django.db import transaction
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from JWTAuth.models import Employee
from course.models import Course, CourseOwned, Section, Lesson, Step, QuizSection, Choice, Quiz, AccessTime, \
    QuizSectionOwned
from dashboard.models import Notification, BalanceHistory
from forum.models import Topic, Forum
from mtf_hackathon.error_handler import PermissionDeniedHandler, ExceptionHandler
from training.models import Training, Schedule, TrainingOwned
from youtube_transcript_api import YouTubeTranscriptApi
from training.views import TrainingListToJSON


def getAvg(employee):
    coursesOwned = CourseOwned.objects.filter(owner=employee)

    data = []
    for courseOwned in coursesOwned :
        courseTotalResult = 0
        countSection = 0
        isWorkingOn = False
        for i in courseOwned.sectionOwned.all() :
            sectionTotalResult = 0
            count = 0
            for j in i.quizSectionOwned.all() :
                if j.attempt != 0 :
                    sectionTotalResult += j.quizResult
                    count += 1
            if count != 0 :
                courseTotalResult += sectionTotalResult/count
                countSection += 1
                isWorkingOn = True

        data.append({
            "id" : courseOwned.course.id,
            "name" : courseOwned.course.name,
            "category" : [j.topic for j in courseOwned.course.topic.all()],
            "date_join" : courseOwned.dateJoined,
            "progress" : courseOwned.totalComplete / courseOwned.course.totalStepAndQuiz if courseOwned.course.totalStepAndQuiz != 0 else 0.0,
            "score" : courseTotalResult/countSection if countSection != 0 else 0,
            "isWorkingOn" : isWorkingOn
        })

    return data


class DashboardView(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try :
            employee = Employee.objects.get(user=request.user)
            if employee.status == 0 :
                raise PermissionDenied("user is not admin")


            dateInput = datetime.now().strftime("%Y-%m-%d")
            date = datetime.strptime(dateInput, "%Y-%m-%d").date()
            dataresp = []
            schedule = Schedule.objects.filter(startTime__date=date)
            for i in schedule:
                data = {
                    "id": i.id,
                    "name": i.training.name,
                    "img": i.training.img.url,
                    "method": i.method,
                    "start_time": i.startTime,
                    "end_time": i.endTime,
                }
                if i.method == 0:
                    data["linkUrl"] = i.linkUrl
                elif i.method == 1:
                    data['location'] = i.location

                dataresp.append(data)



            return Response({
                "status" : 200,
                "message" : "success",
                "data" : {
                    "user_total" : Employee.objects.all().count(),
                    "course_total" : Course.objects.all().count(),
                    "training_total" : Training.objects.all().count(),
                    "training_today" : dataresp,
                }
            })
        except PermissionDenied as e:
            return PermissionDeniedHandler(e)
        except Exception as e :
            return ExceptionHandler(e)

class CourseView(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self,request):
        employee = Employee.objects.get(user=request.user)
        try:
            if employee.status == 0 :
                raise PermissionDenied("user is not admin")


            allCourse = ""
            category = request.GET.get("category")
            search = request.GET.get("search")


            if category or search :
                topicID=[]
                searchQuery = ""
                if search :
                    topicID = [i.id for i in Topic.objects.filter(topic__icontains=search)]
                    searchQuery = search
                categoryObject = Topic.objects.filter(topic=category)
                if len(categoryObject) != 0 :
                    categoryObject = categoryObject[0]
                    allCourse = Course.objects.filter(Q(topic=categoryObject) | Q(topic__in=topicID) | Q(name__icontains=searchQuery)).distinct()
                else :
                    allCourse = Course.objects.filter(
                        Q(topic__in=topicID) | Q(name__icontains=searchQuery)).distinct()

            else :
                allCourse = Course.objects.all()


            dataResp = []
            for i in allCourse :
                data = {
                    "id" : i.id,
                    "name" : i.name,
                    "price" : i.price,
                    "input_date" : i.dateAdded,
                    "user" : CourseOwned.objects.filter(course=i).count()
                }

                if category:
                    data["category"] = [category]
                else:
                    data["category"] = [j.topic for j in i.topic.all()]

                dataResp.append(data)



            return Response({
                "status" : 200,
                "message" : "success",
                "data" : {
                    "course" : dataResp,
                    "count" : len(dataResp)
                }
            })

        except PermissionDenied as e:
            return PermissionDeniedHandler(e)

        except Exception as e:
            return ExceptionHandler(e)



    def post(self, request):
        test = YouTubeTranscriptApi.get_transcript("R9rLCPW-eUI", languages=['id', 'en'])

        employee = Employee.objects.get(user=request.user)
        try:
            with transaction.atomic():
                if employee.status == 0:
                    raise PermissionDenied("user is not admin")

                courseName = request.data['course']['name']
                category = request.data['course']['category']
                img = request.data['course']['img']
                description = request.data['course']['description']
                price = request.data['course']["price"]
                learningPoint = request.data['course']["sylabus"]
                estimateTime = datetime.strptime(request.data['course']["estimate_time"], '%H:%M:%S')

                categoryObject = Topic.objects.filter(topic=category)
                if len(category) == 0 :
                    categoryObject = Topic(topic=category)
                else :
                    categoryObject = Topic.objects.filter(topic=category)

                course = Course(name=courseName, img=img, price =price, description=description, learningPoint=learningPoint, estimateTime=estimateTime)
                course.save()

                for i in categoryObject :
                    course.topic.add(i)


                
                for i in request.data['course']['section'] :
                    sectionTitle = i['title']
                    sectionDescription = i['description']
                    section = Section(title=sectionTitle, description=sectionDescription)
                    section.save()
                    course.section.add(section)

                    for j in i['lesson'] :
                        lessonTitle = j["title"]
                        lesson = Lesson(title=lessonTitle)
                        lesson.save()

                        allStep = []

                        for k in j["step"] :
                            stepTitle = k["title"]
                            stepType = k['type']

                            
                            if stepType == 0 :
                                stepContentText = k["content_text"]
                                stepTimeMinimum = datetime.strptime(k['time_minimum'], '%H:%M:%S')
                                step = Step(title=stepTitle, type=stepType, contentText=stepContentText, timeMinimum=stepTimeMinimum)
                                step.save()
                                allStep.append(step)
                            elif stepType == 1 :
                                stepContentVideo = k["content_video"]
                                stepTimeMinimum = datetime.strptime(k['time_minimum'], '%H:%M:%S')
                                step = Step(title=stepTitle, type=stepType, contentText=stepContentVideo,timeMinimum=stepTimeMinimum)
                                step.save()
                                allStep.append(step)


                        for k in range(len(allStep)) :
                            if len(allStep) == 1 :
                                continue
                            elif k == 0 :
                                allStep[k].nextID = allStep[k+1]
                                allStep[k].save()
                            elif k == (len(allStep) -1)  :
                                allStep[k].prevID = allStep[k - 1]
                                allStep[k].save()
                            else :
                                allStep[k].prevID = allStep[k - 1]
                                allStep[k].nextID = allStep[k+1]
                                allStep[k].save()

                        for k in allStep :
                            lesson.step.add(k)
                            course.totalStepAndQuiz += 1

                        section.lesson.add(lesson)

                    quizTitle = i['quiz']["title"]
                    quizDescription = i['quiz']["description"]
                    quizMinimumScore = i['quiz']["minimum_score"]
                    quizSection = QuizSection(title=quizTitle,
                                              description=quizDescription,
                                              minimumQuizScore=quizMinimumScore
                                              )
                    quizSection.save()
                    section.quizSection = quizSection
                    section.save()

                    for k in i['quiz']["quiz"] :
                        question = k["question"]
                        point = k['point']
                        quizChoice1Object = Choice(choice= k['choice_1']['choice'],
                                                   isRight= True if k['choice_1']["is_right"] == "true" else False )
                        quizChoice2Object = Choice(choice=k['choice_2']['choice'],
                                                   isRight=True if k['choice_2']["is_right"] == "true" else False)
                        quizChoice3Object = Choice(choice=k['choice_3']['choice'],
                                                   isRight=True if k['choice_3']["is_right"] == "true" else False)

                        quizChoice4Object = Choice(choice=k['choice_4']['choice'],
                                                   isRight=True if k['choice_4']["is_right"] == "true" else False)

                        quizChoice1Object.save()
                        quizChoice2Object.save()
                        quizChoice3Object.save()
                        quizChoice4Object.save()

                        quizObject = Quiz(question=question, choice1= quizChoice1Object, choice2=quizChoice2Object, choice3=quizChoice3Object, choice4=quizChoice4Object, point=point)
                        quizObject.save()
                        quizSection.quiz.add(quizObject)
                        course.totalStepAndQuiz += 1

                    course.section.add(section)
                    course.save()
                return Response({
                    "status" : 201,
                    "message" : "success",
                }, status=status.HTTP_201_CREATED)



        except PermissionDenied as e :
            return PermissionDeniedHandler(e)



class TrainingView(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request) :
        try :
            employee = Employee.objects.get(user=request.user)
            if employee.status == 0:
                raise PermissionDenied("user is not admin")

            category = request.GET.get("category")
            search = request.GET.get("search")
            date = request.GET.get("date")

            trainings = None
            setOfTraining = set()
            if category or search or date:
                if category and not search and not date :
                    categoryObject = Topic.objects.filter(topic=category)
                    if len(categoryObject) != 0:
                        categoryObject = categoryObject[0]
                        trainings = Training.objects.filter(
                            Q(topic=categoryObject)).distinct()
                if not category and search and not date:
                    topicID = [i.id for i in Topic.objects.filter(topic__icontains=search)]
                    searchQuery = search
                    trainings = Training.objects.filter(
                        Q(topic__in=topicID) | Q(name__icontains=searchQuery)).distinct()

                if not category and not search and date:
                    dateQuery = datetime.strptime(date, '%Y-%m-%d')
                    schedule = Schedule.objects.filter(startTime__date=dateQuery)
                    for i in schedule :
                        setOfTraining.add(i.training)

                if category and search and not date:
                    categoryObject = Topic.objects.filter(topic=category)
                    topicID = [i.id for i in Topic.objects.filter(topic__icontains=search)]
                    searchQuery = search
                    if len(categoryObject) != 0:
                        categoryObject = categoryObject[0]
                        trainings = Training.objects.filter(
                            Q(topic=categoryObject) &
                            (Q(topic__in=topicID) | Q(name__icontains=searchQuery))
                        ).distinct()

                if category and not search and date :
                    categoryObject = Topic.objects.filter(topic=category)
                    dateQuery = datetime.strptime(date, '%Y-%m-%d')
                    schedule = Schedule.objects.filter(startTime__date=dateQuery)
                    for i in schedule:
                        setOfTraining.add(i.training)
                    newSetOfTraining = set()
                    if len(categoryObject) != 0:
                        categoryObject = categoryObject[0]
                        trainings = Training.objects.filter(
                            Q(topic=categoryObject)).distinct()
                        for i in trainings :
                            newSetOfTraining.add(i)
                        trainings = None
                    setOfTraining = setOfTraining.intersection(newSetOfTraining)

                if not category and search and date:
                    dateQuery = datetime.strptime(date, '%Y-%m-%d')
                    schedule = Schedule.objects.filter(startTime__date=dateQuery)
                    for i in schedule:
                        setOfTraining.add(i.training)

                    topicID = [i.id for i in Topic.objects.filter(topic__icontains=search)]
                    searchQuery = search
                    trainings = Training.objects.filter(
                        Q(topic__in=topicID) | Q(name__icontains=searchQuery)).distinct()

                    newSetOfTraining = set()
                    for i in trainings:
                        newSetOfTraining.add(i)
                    trainings = None
                    setOfTraining = setOfTraining.intersection(newSetOfTraining)

                if category and search and date :
                    dateQuery = datetime.strptime(date, '%Y-%m-%d')
                    schedule = Schedule.objects.filter(startTime__date=dateQuery)
                    for i in schedule:
                        setOfTraining.add(i.training)

                    categoryObject = Topic.objects.filter(topic=category)
                    topicID = [i.id for i in Topic.objects.filter(topic__icontains=search)]
                    searchQuery = search
                    if len(categoryObject) != 0:
                        categoryObject = categoryObject[0]
                        trainings = Training.objects.filter(
                            Q(topic=categoryObject) &
                            (Q(topic__in=topicID) | Q(name__icontains=searchQuery))
                        ).distinct()

                    newSetOfTraining = set()

                    for i in trainings:
                        newSetOfTraining.add(i)
                    trainings = None
                    setOfTraining = setOfTraining.intersection(newSetOfTraining)

            else :
                trainings = Training.objects.all()

            if trainings :
                for i in trainings:
                    setOfTraining.add(i)



            dataResp = []

            for i in setOfTraining :
                schedule = None
                for j in Schedule.objects.filter(training=i).order_by('startTime') :
                    if j.startTime > (timezone.now() + timezone.timedelta(hours=7)):
                        schedule = j
                        break
                if not schedule :
                    schedule = "Jadwal telah terlewati"

                topicInput = request.GET.get("topic")
                topic = Topic.objects.filter(topic=topicInput)
                topicResponse= []
                if len(topic) == 1 :
                    topicResponse.append(topic[0].topic)
                else :
                    topicResponse = [j.topic for j in i.topic.all()]

                data = {
                    "id" : i.id,
                    "name" : i.name,
                    "img" : i.img.url,
                    "organizer" : i.organizer,
                    "topic" : topicResponse,
                    "schedule" : schedule if isinstance(schedule, str) else {"start_time" : schedule.startTime, "end_time" : schedule.endTime },
                    "user_count" : TrainingOwned.objects.filter(training=i).count()
                }
                dataResp.append(data)

            return Response({
                "status" : 200,
                "message" : "success",
                "data" : dataResp
            })


        except PermissionDenied as e :
            return PermissionDeniedHandler(e)

    def post(self, request):
        try:
            with transaction.atomic():
                employee = Employee.objects.get(user=request.user)
                if employee.status == 0:
                    raise PermissionDenied("user is not admin")

                trainingInput = request.data["training"]
                name = trainingInput['name']
                topic = trainingInput["topic"]
                img = trainingInput["img"]
                organizer = trainingInput["organizer"]
                about = trainingInput["about"]

                topicObject = Topic.objects.filter(topic=topic)
                if len(topicObject) == 0 :
                    newTopic = Topic.objects.create(topic=topic)
                    topicObject = Topic.objects.filter(topic=topic)
                else :
                    topicObject = Topic.objects.filter(topic=topic)

                training = Training.objects.create(name=name, organizer=organizer, img=img, about=about)
                for i in topicObject :

                    training.topic.add(i)


                startTime = datetime.strptime(trainingInput["schedule"]["start_time"], '%Y-%m-%d %H:%M:%S')
                endTime =  datetime.strptime(trainingInput["schedule"]["end_time"], '%Y-%m-%d %H:%M:%S')
                method = trainingInput["method"]

                schedule = None
                if method == 0 :
                    linkUrl = trainingInput["link_url"]
                    schedule = Schedule.objects.create(title=name,
                                                       startTime=startTime,
                                                       endTime=endTime,
                                                       training=training,
                                                       method=method,
                                                       linkUrl=linkUrl
                                                       )
                else :
                    location = trainingInput["location"]
                    schedule = Schedule.objects.create(title=name,
                                                       startTime=startTime,
                                                       endTime=endTime,
                                                       training=training,
                                                       method=method,
                                                       location=location
                                                       )


                for i in trainingInput["participant"] :
                    owner = Employee.objects.get(user__username=i['username'])
                    trainingOwned = TrainingOwned.objects.create(owner=owner, training=training)
                    notif = Notification.objects.create(owner=owner, notif="Kamu telah terdaftar pada pelatihan " + trainingOwned.training.name, category="Pelatihan")

            return Response({
                "status" : 201,
                "message" : "success",
            }, status=status.HTTP_201_CREATED)




        except PermissionDenied as e :
            return PermissionDeniedHandler(e)

        except Exception as e :
            return ExceptionHandler(e)

class EmployeeView(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            employee = Employee.objects.get(user=request.user)
            if employee.status==0:
                raise PermissionDenied("user is not admin")

            dataResp = []
            allEmployee = Employee.objects.all()

            filterDivisi = request.GET.get("divisi")
            filterSearch = request.GET.get("search")
            if filterDivisi and not filterSearch:
                allEmployee = Employee.objects.filter(department__icontains=filterDivisi)
            if not filterDivisi and filterSearch :
                allEmployee = Employee.objects.filter(Q(user__first_name__icontains=filterSearch) |
                                                      Q(user__last_name__icontains=filterSearch) |
                                                      Q(user__username__icontains=filterSearch) |
                                                      Q(user__email__icontains=filterSearch))
            if filterDivisi and filterSearch :
                allEmployee = Employee.objects.filter((Q(user__first_name__icontains=filterSearch) |
                                                      Q(user__last_name__icontains=filterSearch) |
                                                      Q(user__username__icontains=filterSearch) |
                                                      Q(user__email__icontains=filterSearch)) &
                                                      Q(department__icontains=filterDivisi))

            for i in allEmployee:
                dataResp.append({
                    "username" : i.user.username,
                    "email" : i.user.email,
                    "first_name" : i.user.first_name,
                    "last_name" : i.user.last_name,
                    "department" : i.department,
                    "start_work_date" : i.start_work_date,
                })

            return Response({
                "status" : 200,
                "message" : "success",
                "data" : dataResp
            }, status=status.HTTP_200_OK)
        except PermissionDenied as e :
            return PermissionDeniedHandler(e)


class EmployeeDetailView(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        try:
            admin = Employee.objects.get(user=request.user)
            if admin.status==0:
                raise PermissionDenied("user is not admin")


            employee = Employee.objects.get(user__username=username)
            courseOwned = CourseOwned.objects.filter(owner=employee)

            courseData = getAvg(employee)
            trainingdata = []
            for i in TrainingOwned.objects.filter(owner=employee) :
                data = {
                    "id" : i.training.id,
                    "name" : i.training.name,
                    "category" : [j.topic for j in i.training.topic.all()]
                }

                schedule = None
                for j in Schedule.objects.filter(training=i.training):
                    if j.startTime > (timezone.now() + timezone.timedelta(hours=7)) :
                        schedule = j.startTime
                        break

                if not schedule :
                    schedule = "jadwal telah terlewati"

                data["schedule"] = schedule

                trainingdata.append(data)





            allCourseOwned = []
            for i in courseOwned :
                accessTime = AccessTime.objects.filter(owner=employee, course=i)
                accessTimeDetail = []
                total = 0
                if len(accessTimeDetail) == 0:
                    total = 0
                else:
                    total = 0
                    for i in accessTime:
                        total += int(i.duration.minutes)
                        accessTimeDetail.append({
                            "access_time": i.duration.minutes,
                            "date": i.date.strftime("%Y-%m-%d")
                        })


                allCourseOwned.append({
                    "id" : i.course.id,
                    "total_acces_time" : total,
                    "access_time_detail" : accessTimeDetail
                })


            return Response({
                "status" : 200,
                "message" : "success",
                "data" : {
                    "username" : employee.user.username,
                    "email" : employee.user.email,
                    "first_name" : employee.user.first_name,
                    "last_name" : employee.user.last_name,
                    "img" : employee.img.url,
                    "department" : employee.department,
                    "position" : employee.posistion,
                    "course" : {
                        "course" : courseData,
                        "count" : len(courseData)
                    },
                    "training" : {
                        "training" : trainingdata,
                        "count" : len(trainingdata)
                    },
                }
            })

        except PermissionDenied as e :
            return PermissionDeniedHandler(e)


class PewiraMilesBalanceView(APIView) :

    data_input = {
        "username" : "testing",
        "nominal" : 40.0,
        "notes" : "testing"
    }
    permission_classes = [IsAuthenticated]
    def post(self, request):

        try :
            admin = Employee.objects.get(user=request.user)
            if admin.status == 0:
                raise PermissionDenied("user is not admin")
            username = request.data["username"]
            nominal = request.data["nominal"]
            notes = request.data["notes"]

            employee = Employee.objects.get(user__username=username)
            employee.pewiraMilesBalance += nominal

            historyBalance = BalanceHistory.objects.create(owner=employee, description=notes, balance=nominal, type="Admin")
            notification = Notification.objects.create(owner=employee, notif="Kamu mendapat hadiah dari Admin", category="Pewira Miles Balance")

            return Response({
                "status" : 201,
                "message" : "succes",
            }, status=status.HTTP_201_CREATED)
        except PermissionDenied as e :
            return PermissionDeniedHandler(e)
