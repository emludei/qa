# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', None)


class QABase(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL)
    body = models.TextField(verbose_name='Body')
    pub_date = models.DateTimeField(verbose_name='Publication date', auto_now_add=True)

    class Meta:
        abstract = True


class Question(QABase):
    title = models.CharField(verbose_name='Title', max_length=250)

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.title)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'questions'


class Answer(QABase):
    question = models.ForeignKey(Question)
    accepted = models.BooleanField(verbose_name='Is accepted by topic starter', default=False)

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'pk': self.question.pk})

    def __str__(self):
        return '<Answer to: %s>' % (self.question.title,)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answers'
