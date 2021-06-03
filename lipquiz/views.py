from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import VideoQuiz
from results.models import SingleWordResult
from questions.models import SingleWordQuestion
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
    response = list()
    for q in videoquiz.get_questions():
        answers = list()
        for a in q.get_answers():
            answers.append(a.text)
        #questions.append({str(q.pk) + " " + q.text : answers})
        print(f"Video path: {q.video_path}")
        response.append({'question': q.text, 'video_path': q.video_path, 'answer': answers})
        questions.append({q.video_path : answers})

    print(f"Response: {response}")
    return JsonResponse(response, safe=False)

def video_quiz_data_save(request, pk):
    if request.is_ajax():
        data = request.POST
        data = dict(data.lists())
        data.pop('csrfmiddlewaretoken')

        quiz = VideoQuiz.objects.get(pk=pk)
        user = request.user

        results = list()
        score = 0
        score_multiplier = 100/quiz.number_of_questions

        for q in data.keys():
            question = SingleWordQuestion.objects.get(video_path=q)
            answers = question.get_answers()
            for a in answers:
                if a.correct:
                    correct_answer = a.text
            user_answered = data[q][0]
            if correct_answer == user_answered:
                score += 1
            results.append({str(question.text):{"correct_answer":correct_answer, "answered":user_answered}})
        
        score_ = score_multiplier * score
        print(f"Score: {score_}")

        SingleWordResult.objects.create(quiz=quiz, user=user, score=score_)

        return JsonResponse({'score': score_, 'results': results})