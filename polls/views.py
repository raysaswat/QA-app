from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from .models import Choice, Question
from .serializers import ChoiceSerializer, QuestionSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
   
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


class ListChoiceView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    
class ListQuestionView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer