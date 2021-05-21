from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import VideoQuiz
from django.http import JsonResponse

# Create your views here.
class VideoQuizListView(ListView):
    model = VideoQuiz 
    template_name = "lipquiz/main.html"

def video_quiz_view(request, pk):
    videoquiz = VideoQuiz.objects.get(pk=pk)
    return render(request, 'lipquiz/quiz.html', {'obj': videoquiz})

# Returns the content of the quiz
def video_quiz_data_view(request, pk):
    videoquiz = VideoQuiz.objects.get(pk=pk)
    questions = list()
    for q in videoquiz.get_questions():
        answers = list()
        for a in q.get_answers():
            answers.append(a.text)
        #questions.append({str(q.pk) + " " + q.text : answers})
        print(f"Video path: {q.video_path}")
        questions.append({q.video_path : answers})

    return JsonResponse({
        'data': questions, 
        'time': videoquiz.time,
    })