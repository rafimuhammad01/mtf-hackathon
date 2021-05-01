from django.conf.global_settings import MEDIA_ROOT
from django.db import models
from forum.models import Topic
from ckeditor.fields import RichTextField
from forum.models import Forum
from JWTAuth.models import Employee
from cloudinary.models import CloudinaryField
# Create your models here.

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
    totalRating = models.ManyToManyField(Employee, blank=True)
    estimateTime = models.TimeField()
    totalParticipant = models.IntegerField(default=0)
    forum = models.ForeignKey(Forum, blank=True, on_delete=models.CASCADE)
    totalStepAndQuiz = models.FloatField(default=0)

    def __str__(self) :
        return self.name

class Section(models.Model) :
    title = models.CharField(max_length=50)
    quizSection = models.ForeignKey('QuizSection', blank=True, on_delete=models.CASCADE, null=True)
    lesson = models.ManyToManyField('Lesson', blank=True)
    description = models.TextField(max_length=255, blank=True)

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
    timeMinimum = models.TimeField()
    prevID = models.ForeignKey('Step', on_delete=models.CASCADE, blank=True, null=True, related_name="idPrev")
    nextID = models.ForeignKey('Step', on_delete=models.CASCADE, blank=True, null=True, related_name="idNext")

    def __str__(self):
        return self.title

class QuizSection(models.Model) :
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    quiz = models.ManyToManyField("Quiz")
    minimumQuizScore = models.FloatField(default=0)

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


class CourseOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.FloatField(default=0.0)
    totalComplete = models.FloatField(default=0)
    isComplete = models.BooleanField(default=False)
    lastLesson = models.ForeignKey(Lesson, blank=True, null=True, on_delete=models.CASCADE)
    lastStep = models.ForeignKey(Step, blank=True, null=True, on_delete=models.CASCADE)
    lastQuiz = models.ForeignKey(QuizSection, blank=True, null=True, on_delete=models.CASCADE)
    sectionOwned = models.ManyToManyField('SectionOwned', blank=True)
    notes = models.ManyToManyField('Notes', blank=True)

    def __str__(self):
        return str(self.owner) + str(self.course)

class SectionOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    isComplete = models.BooleanField(default=False)
    lessonOwned = models.ManyToManyField('LessonOwned', blank=True)
    quizSectionOwned = models.ManyToManyField('QuizSectionOwned', blank=True )

    def __str__(self):
        return str(self.owner) + str(self.section)


class QuizSectionOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    quizSection = models.ForeignKey(QuizSection, on_delete=models.CASCADE, null=True)
    isComplete = models.BooleanField(default=False)
    quizResult = models.FloatField(default=0.0, blank=True)
    isPassedQuiz = models.BooleanField(default=False)
    quizOwned = models.ManyToManyField('QuizOwned', blank=True, null=True)
    attempt = models.IntegerField(default=0)

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
    stepOwned = models.ManyToManyField('StepOwned', blank=True)

    def __str__(self):
        return str(self.owner) + str(self.lesson)

class StepOwned(models.Model) :
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    timeConsume = models.TimeField(blank=True, null=True)
    isComplete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner) + str(self.step)

class Notes(models.Model) :
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    highlightText = models.TextField(max_length=255)
    notes = models.TextField(max_length=255)