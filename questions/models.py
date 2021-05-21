from django.db import models
from quizzes.models import Quiz
from lipquiz.models import VideoQuiz

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    # For a question, we need different answer choices 
    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question : {self.question.text}, Answer : {self.text}, Correct : {self.correct}"


class SingleWordQuestion(models.Model):
    text = models.CharField(max_length=200)
    video_path = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(VideoQuiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return singlewordanswer_set.all()

class SingleWordAnswer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(SingleWordQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question: {self.question}, Answer: {self.text}, Correct: {self.correct}"