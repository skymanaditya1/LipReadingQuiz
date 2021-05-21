from django.urls import path
from . import views

urlpatterns = [
    path('', views.VideoQuizListView.as_view(), name='lip-quiz-view'),
    path('<pk>/', views.video_quiz_view, name='video-quiz-view'),
]