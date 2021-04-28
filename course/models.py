from django.conf.global_settings import MEDIA_ROOT
from django.db import models
from forum.models import Topic
from ckeditor.fields import RichTextField
from forum.models import Forum
from JWTAuth.models import Employee
from cloudinary.models import CloudinaryField
# Create your models here.
class Training(models.Model):
    name = models.CharField(max_length=50)
    schedule = models.ManyToManyField('Schedule', blank=True)
    img = CloudinaryField('image')

    def __str__(self) :
        return self.name

class Schedule(models.Model) :
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    startTime = models.TimeField()
    endTime = models.TimeField()

    def __str__(self) :
        return self.title

class Course(models.Model) :
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    topic = models.ManyToManyField(Topic, blank=True)
    img = CloudinaryField('image')
    section  = models.ManyToManyField('Section')
    price = models.FloatField(default=0)
    reward = models.FloatField(default=0)
    about = RichTextField(blank=True)
    learningPoint = RichTextField(blank=True)
    rating = models.FloatField(default=0)
    estimateTime = models.TimeField(default=0)
    forum = models.ForeignKey(Forum, blank=True, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

class Section(models.Model) :
    LESSON = 0
    QUIZ = 1
    SECTION_TYPES = [
        (LESSON, "Lesson"),
        (QUIZ, "Quiz"),
    ]

    title = models.CharField(max_length=50)
    type = models.IntegerField(choices=SECTION_TYPES)
    quiz = models.ManyToManyField('Quiz', blank=True)
    lesson = models.ManyToManyField('Lesson', blank=True)
    description = models.TextField(max_length=255, blank=True)
    minimumQuizScore = models.FloatField(default=0)

    def __str__(self) :
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=50)
    step = models.ManyToManyField('Step', blank=True)

    def __str__(self):
        return self.title

class Step(models.Model) :
    TEXT = 0
    VIDEO = 1
    STEP_TYPES = [
        (TEXT, "Text"),
        (VIDEO, "Video"),
    ]
    title = models.CharField(max_length=50)
    type = models.IntegerField(choices=STEP_TYPES)
    contentText = RichTextField(blank=True)
    contentVideo = models.URLField(blank=True)
    transcript = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Quiz(models.Model) :
    question  = models.CharField(max_length=50)
    choice1 = models.ForeignKey('Choice', blank=True, on_delete=models.CASCADE, related_name='choice1')
    choice2 = models.ForeignKey('Choice', blank=True, on_delete=models.CASCADE, related_name='choice2')
    choice3 = models.ForeignKey('Choice', blank=True, on_delete=models.CASCADE, related_name='choice3')
    choice4 = models.ForeignKey('Choice', blank=True, on_delete=models.CASCADE, related_name='choice4')
    point = models.FloatField(default=0.0)

    def __str__(self):
        return self.question

class Choice(models.Model) :
    choice = models.CharField(max_length=50)
    isRight = models.BooleanField(default=False)
    def __str__(self):
        return self.choice

class TrainingOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.owner) + str(self.training)

class CourseOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.FloatField(default=0.0)
    isComplete = models.BooleanField(default=False)
    lastLesson = models.ForeignKey(Lesson, blank=True, on_delete=models.CASCADE)
    sectionOwned = models.ForeignKey('SectionOwned', blank=True, on_delete=models.CASCADE)
    notes = models.ManyToManyField('Notes', blank=True)

    def __str__(self):
        return str(self.owner) + str(self.course)

class SectionOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    quizResult = models.FloatField(default=0.0, blank=True)
    isComplete = models.BooleanField(default=False)
    isPassedQuiz = models.BooleanField(default=False)
    lessonOwned = models.ForeignKey('LessonOwned', blank=True, null=True, on_delete=models.CASCADE)
    quizOwned = models.ForeignKey('QuizOwned', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.owner) + str(self.section)

class QuizOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    isRight = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner) + str(self.quiz)

class LessonOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    isComplete = models.BooleanField(default=False)
    stepOwned = models.ForeignKey('StepOwned', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.owner) + str(self.lesson)

class StepOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    timeConsume = models.TimeField(default=0)
    isComplete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner) + str(self.step)

class Notes(models.Model) :
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    highlightText = models.TextField(max_length=255)
    notes = models.TextField(max_length=255)