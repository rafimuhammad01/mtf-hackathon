from django.db import models
from forum.models import Topic
from ckeditor.fields import RichTextField

# Create your models here.
class ArticleSection(models.Model):
    topic = models.ManyToManyField(Topic, blank=True)
    title = models.CharField(max_length=50)
    section = models.ManyToManyField('Article', blank=True)

    def __str__(self) :
        return self.title


class Article(models.Model) :
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True)

    def __str__(self) :
        return self.title
