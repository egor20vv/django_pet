from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/', views.polls, name='polls'),
    path('polls/<int:question_id>/', views.detail, name='details'),
    path('polls/<int:question_id>/result/', views.result, name='result'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]
