from django.shortcuts import render, get_object_or_404
from .models import Question
from django.http import Http404

# This is a simple view
def index(request):
    # get first 5 questions
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# def result(request, question_id):
#     return HttpResponse("You're looking for result of question with id %s.", %question_id)
    
# def vote(request, question_id):
#     return HttpResponse("You're voting for question with id %s.", %question_id)