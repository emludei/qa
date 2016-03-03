from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from .forms import QuestionForm
from .models import Question, Answer


class PostQuestion(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'post-question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostQuestion, self).form_valid(form)


class PostAnswer(CreateView):
    model = Answer
    fields = ['body']

    def form_valid(self, form):
        form.instance.question = Question.objects.get(pk=self.kwargs['question_pk'])
        form.instance.author = self.request.user
        return super(PostAnswer, self).form_valid(form)


class AcceptAnswerView(View):
    def get(self, request, answer_pk):
        answer = Answer.objects.get(pk=answer_pk)

        accepted_on_this_question = Answer.objects.filter(question=answer.question)

        if accepted_on_this_question.exists():
            accepted_on_this_question.update(accepted=False)

        answer.accepted = True
        answer.save()

        return redirect('question-detail', pk=answer.question.pk)


class QuestionListView(ListView):
    model = Question
    template_name = 'question-list.html'
    context_object_name = 'questions'
    paginate_by = 50


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question-detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['answers'] = Answer.objects.filter(question=context['question'])
        return context
