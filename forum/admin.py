from django.contrib import admin
from .models import Forum, Answer, Topic

# Register your models here.
admin.site.register(Forum)
admin.site.register(Answer)
admin.site.register(Topic)