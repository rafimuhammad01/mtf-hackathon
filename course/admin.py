from django.contrib import admin
from course.models import Course, Section, Lesson, Step, Quiz, Choice, CourseOwned, \
    SectionOwned, QuizOwned, LessonOwned, StepOwned, Notes, QuizSection, QuizSectionOwned

# Register your models here.
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(Step)
admin.site.register(Quiz)
admin.site.register(Choice)
admin.site.register(CourseOwned)
admin.site.register(SectionOwned)
admin.site.register(QuizOwned)
admin.site.register(LessonOwned)
admin.site.register(StepOwned)
admin.site.register(QuizSection)
admin.site.register(QuizSectionOwned)
admin.site.register(Notes)

