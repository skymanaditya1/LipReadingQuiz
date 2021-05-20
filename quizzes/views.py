from django.shortcuts import render
from django.views.generic import ListView
from .models import Quiz
from django.http import JsonResponse
from questions.models import Question
from results.models import Result

# Create your views here.
# This shows all the quizzes in the form of a listview 
class QuizListView(ListView):
    model = Quiz 
    template_name = 'quizzes/main.html'

# Get the quiz corresponding to the primary key
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizzes/quiz.html', {'obj':quiz})

# Returns the quiz data view
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})

    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

# Save the quiz response 
def save_quiz_view(request, pk):
    questions = list()
    if request.is_ajax():
        data = request.POST
        data = dict(data.lists())
        data.pop('csrfmiddlewaretoken')
        for k in data.keys():
            question = Question.objects.get(text=k)
            questions.append(question)

        # compute the score for the user on the quiz 
        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        # In the results, we want to show the answered choice and the correct answer
        results = list()
        score_multiplier = 100 / quiz.number_of_questions
        score = 0

        for question in questions:
            answers = question.get_answers()
            for answer in answers:
                if answer.correct:
                    correct_answer = answer.text
            selected_answer = data[question.text][0]
            if correct_answer == selected_answer:
                score += 1
            results.append({str(question): {"correct_answer":correct_answer, "answered": selected_answer}})

        score_ = score_multiplier * score 
        print(f"Score : {score_}%")

        # update the results entry with the score for (user, quiz)
        Result.objects.create(quiz=quiz, user=user, score=score_)

        return JsonResponse({'passed': score_ >= quiz.pass_score, 'score': score_, 'results': results})