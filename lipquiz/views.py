from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import VideoQuiz

# Create your views here.
class VideoQuizListView(ListView):
    model = VideoQuiz 
    template_name = "lipquiz/main.html"

def video_quiz_view(request, pk):
    videoquiz = VideoQuiz.objects.get(pk=pk)
    return render(request, 'lipquiz/quiz.html', {'obj': videoquiz})