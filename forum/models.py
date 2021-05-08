from datetime import datetime
from django.db import models
from JWTAuth.models import Employee

# Create your models here.


class Forum(models.Model):
    title = models.CharField(max_length=50)
    question = models.TextField(max_length=500)
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="forum_owner")
    course = models.ForeignKey('course.Course', null=True, blank=True, on_delete=models.CASCADE, related_name="course_owner")
    answer = models.ManyToManyField('Answer', blank=True)
    topic = models.ManyToManyField('Topic', blank=True)
    upvote = models.ManyToManyField(Employee, blank=True)
    createdAt = models.DateTimeField(default=datetime.now())

    def __str__(self) :
        return self.title


class Answer(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="answer_owner")
    answer = models.TextField(max_length=500)
    upvote = models.ManyToManyField(Employee, blank=True)
    createdAt = models.DateTimeField(default=datetime.now())

    def __str__(self) :
        return self.answer

class Topic(models.Model) :
    id = models.IntegerField(primary_key=True)
    topic = models.CharField(max_length=50)

    def __str__(self) :
        return self.topic