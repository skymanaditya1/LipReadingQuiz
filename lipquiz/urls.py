from django.urls import path
from . import views

app_name = 'lipquiz'

urlpatterns = [
    path('', views.VideoQuizListView.as_view(), name='lip-quiz-view'),
    path('lipread_sentences/<pk>/', views.video_quiz_view, name='video-quiz-view'),
    path('lipread_sentences/<pk>/data/', views.video_quiz_data_view, name='video-quiz-data-view'),
    path('lipread_sentences/<pk>/save/', views.video_quiz_data_save, name='video-quiz-data-save'),
    path('', views.MissingWordsQuizListView.as_view(), name='lip-missing-words-quiz-view'),
    path('lipread_missing/<pk>/', views.video_missing_words_quiz_view, name='video-missing-words-quiz-view'),
    path('lipread_missing/<pk>/data/', views.video_missing_words_quiz_data_view, name='video-missing-words-quiz-data-view'),
    path('lipread_missing/<pk>/save/', views.video_missing_words_quiz_data_save, name='video-missing-words-quiz-data-save'),
    # path('lipread_words', views.lipread_words, name='lipread-words'),
    path('lipread_missing/', views.lipread_words, name='lipread-words'),
]