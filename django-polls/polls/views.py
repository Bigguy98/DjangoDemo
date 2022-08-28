from time import timezone
from django.shortcuts import render, get_object_or_404
from .models import Answer, Question
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# view as class
# so ListView and DetailView is django defaul view
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(generic.DeleteView):
    model = Question
    template_name = 'polls/result.html' 
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.answer_set.get(pk=request.POST['choice'])
        print(request.POST['choice'])
        print(request)
    except (KeyError, Answer.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))
        # return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))