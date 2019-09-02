from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Choice
from django.shortcuts import render


def index(request):         #model and DB
    question=Question.objects.get(pk=1)
    return render(
    request,
    'polls/index.html',
    {'questions':Question.objects.all()})    #template
