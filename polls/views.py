import time

from django.db.models import F
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your views here.
from django.views import View, generic

from .models import Question, Choice


def index(request):
    # 根据发布日期排序的最近5个投票问题
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 创建context 上下文
    context = {
        'latest_question_list': latest_question_list,
    }
    # 加载模板
    template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    # 使用快捷函数render()
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {
                          'question': question,
                          'error_message': "you didn't select a choice."
                      })
    else:
        # 使用F函数避免竞争条件, 解决多个线程同时操作结果数混乱
        selected_choice.votes = F('votes') + 1
        # time.sleep(3)
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


# ## 通用视图

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        返回最近5个发布的问题 不包含未来日期
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:20]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
