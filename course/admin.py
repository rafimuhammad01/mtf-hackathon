from django.contrib import admin
from course.models import Training, Schedule, Course, Section, Lesson, Step, Quiz, Choice, TrainingOwned, CourseOwned, \
    SectionOwned, QuizOwned, LessonOwned, StepOwned, Notes

# Register your models here.


admin.site.register(Training)
admin.site.register(Schedule)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(Step)
admin.site.register(Quiz)
admin.site.register(Choice)
admin.site.register(TrainingOwned)
admin.site.register(CourseOwned)
admin.site.register(SectionOwned)
admin.site.register(QuizOwned)
admin.site.register(LessonOwned)
admin.site.register(StepOwned)
admin.site.register(Notes)

