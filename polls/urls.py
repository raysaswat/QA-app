from django.urls import path

from . import views
from .views import ListChoiceView
from .views import ListQuestionView

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('choice/', ListChoiceView.as_view(), name="choice-all"),
    path('question/', ListQuestionView.as_view(), name="question-all")
]