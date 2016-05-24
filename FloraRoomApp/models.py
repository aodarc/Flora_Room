from django.db import models
from django.contrib.auth.models import User


# Create your models here.
SHORT_TEXT = 2300


class Article(models.Model):
    class Meta:
        ordering = ('-create_date',)

    title = models.CharField(max_length=255, blank=False, verbose_name=u'Заголовок', db_index=True, unique=True)
    text = models.TextField(max_length=2000, blank=False, verbose_name=u'Текст статті')
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(User)
    like = models.IntegerField(default=0, null=False, verbose_name=u'Вподобання')
    is_posted = models.BooleanField(default=0, verbose_name=u'Опублікована?')
    category = models.ForeignKey('Category')

    def __str__(self):
        return self.title

    def short(self):
        if len(self.text) > SHORT_TEXT:
            return self.text[:SHORT_TEXT] + ' ......'
        else:
            return self.text


class Comment(models.Model):
    article = models.ForeignKey(Article)
    text = models.TextField(max_length=1000, verbose_name=u'Текст коментаря')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user.username + ' >>> ' + self.text[:40]


class Category(models.Model):
    category = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return self.category
