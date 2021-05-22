from django.urls import path
from . import views

app_name = 'lipquiz'

urlpatterns = [
    path('', views.VideoQuizListView.as_view(), name='lip-quiz-view'),
    path('<pk>/', views.video_quiz_view, name='video-quiz-view'),
    path('<pk>/data/', views.video_quiz_data_view, name='video-quiz-data-view'),
    path('<pk>/save/', views.video_quiz_data_save, name='video-quiz-data-save'),
]