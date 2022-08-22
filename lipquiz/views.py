from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import MissingWordInSentenceQuiz, VideoQuiz
from results.models import MissingWordsResult, SingleWordResult
from questions.models import MissingWordsAnswer, MissingWordsQuestion, SingleWordQuestion
from django.http import JsonResponse
import random

# View corresponding to lipreading isolated words protocol
class VideoQuizListView(ListView):
    model = VideoQuiz 
    template_name = "lipquiz/main.html"

# View corresponding to lirpeading missing words in sentences protocol 
class MissingWordsQuizListView(ListView):
    model = MissingWordInSentenceQuiz
    template_name = "lipquiz/main_missingwords.html"

# loads the quiz view corresponding to the primary key 
# in obj, the fields defined in the VideoQuiz model are loaded 
def video_quiz_view(request, pk):
    videoquiz = VideoQuiz.objects.get(pk=pk)
    return render(request, 'lipquiz/quiz.html', {'obj': videoquiz})

# load the quiz view corresponding to the primary key for the protocol 
# -- lipreading missing words in sentences 
def video_missing_words_quiz_view(request, pk):
    videoquiz = MissingWordInSentenceQuiz.objects.get(pk=pk)
    return render(request, 'lipquiz/missingword_quiz.html', {'obj': videoquiz})

# Returns the content of the quiz corresponding to the lipreading isolated words protocol
# This is used when the user navigates inside the quiz
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

# returns the content of the quiz corresponding to the protocol -- lipreading missing words in sentence
# This is used when the user is inside the quiz
def video_missing_words_quiz_data_view(request, pk):
    # we need the questions and answers corresponding to a given quiz
    videoquiz = MissingWordInSentenceQuiz.objects.get(pk=pk)
    questions = list()
    response = list()

    print(f'This function gets called when the quiz is loaded')

    # get all questions corresponding to a given video quiz
    for question in videoquiz.get_questions():
        # get the answer corresponding to the given question 
        answers = list()
        for answer in question.get_answers():
            answers.append(answer.answer)

        print(f'Answers are : {answers}')

        print(f'Video path : {question.video_path}')
        response.append({'question': question.text, 'video_path': question.video_path, 'answer': answers})
        questions.append({question.video_path: answer}) # assigning an answer to a question key (video_path)

    print(f'Response : {response}')
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


def video_missing_words_quiz_data_save(request, pk):
    print(request.POST)
    if request.is_ajax():
        questions = list()
        data = request.POST
        data_ = dict(data.lists()) # transforms the query dict to an ordinary list
        # remove the csrfmiddlewaretoken from the dict of question-answer pair 
        data_.pop('csrfmiddlewaretoken')
        
        quiz = MissingWordInSentenceQuiz.objects.get(pk=pk)
        user = request.user

        total_questions = quiz.number_of_questions
        print(f'Number of questions in the quiz : {total_questions}')

        correct = 0
        total_questions = 0
        results = list()     

        for q in data_.keys():
            print('key: ', q)
            question = MissingWordsQuestion.objects.get(video_path=q)
            answers = question.get_answers()
            user_answered = data[q].lower()
            answer = answers[0].answer.lower()
            print(f'Correct answer : {answer}, user answered : {user_answered}')
            # questions.append(question)

            # for each question if the answered question is the correct answer 
            if answer == user_answered:
                print(f'{answer.lower()}, {user_answered.lower()}')
                correct += 1

            total_questions += 1

            results.append({str(question.text):{"correct_answer":answer, "answered":user_answered}})

        score = (correct/total_questions)*100
        print(f'Total questions : {total_questions}, correctly answered : {correct}, score is : {score}')
        
        MissingWordsResult.objects.create(quiz=quiz, user=user, score=score)

    return JsonResponse({'score': score, 'results': results})


def lipread_words(request):
    print(f'Inside this function')
    lipread_words_quizzes = MissingWordInSentenceQuiz.objects.all().filter(is_visible=True)
    print(f'Lipread word quizzes : {lipread_words_quizzes}')

    # randomly choose one quiz from the list of quizzes 
    words_quiz_list = list(lipread_words_quizzes)
    random.shuffle(words_quiz_list)
    words_quiz = words_quiz_list[0]
    
    print(f'Word quiz list : {str(words_quiz)}')

    pk, name, description, num_questions, difficulty, _ = str(words_quiz).split(';')
    print(f'Fields are : {type(pk)}, {name}, {description}')

    pk = int(pk)
    print(f'The primary key is : {pk}, and type is : {type(pk)}')

    videoquiz = VideoQuiz.objects.get(id=pk)
    print(f'Video quiz is : {videoquiz}')
    return render(request, 'lipquiz/missingword_quiz.html', {'obj': videoquiz})


def lipread_sentences(request):
    pass


def lipread_missing(request):
    pass