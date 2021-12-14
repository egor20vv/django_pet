from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def polls(request):
    latest_question_list = Question.objects.order_by('-pub_data')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})
    # return HttpResponse("You're looking at the result of a question {}".format(question_id))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        selected_choice.refresh_from_db()

        redirect_path = reverse('polls:result', args=(question.id,))
        return HttpResponseRedirect(redirect_path)
