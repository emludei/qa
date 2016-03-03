# -*- coding: utf-8 -*-

from django.conf.urls import url

import views


urlpatterns = [
    url(r'^questions/$', views.QuestionListView.as_view(), name='questions'),
    url(r'^post-question/$', views.PostQuestion.as_view(), name='post-question'),
    url(r'^question-detail/(?P<pk>\d+)/$', views.QuestionDetailView.as_view(), name='question-detail'),

    url(r'^post-answer/(?P<question_pk>\d+)/$', views.PostAnswer.as_view(), name='post-answer'),
    url(r'^accept-answer/(?P<answer_pk>\d+)/$', views.AcceptAnswerView.as_view(), name='accept-answer'),
]
