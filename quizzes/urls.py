from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
)

app_name = 'quizzes'

# These application specific url patterns need to be added to the project URLs
urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-quiz'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]