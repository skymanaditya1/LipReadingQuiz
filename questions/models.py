from django.db import models
from quizzes.models import Quiz
from lipquiz.models import MissingWordInSentenceQuiz, VideoQuiz
import random

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


# Model corresponding to the protocol -- Single word question
class SingleWordQuestion(models.Model):
    text = models.CharField(max_length=200)
    video_path = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(VideoQuiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        answers = list(self.singlewordanswer_set.all())
        random.shuffle(answers)
        return answers

class SingleWordAnswer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(SingleWordQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question: {self.question}, Answer: {self.text}, Correct: {self.correct}"

# Model corresponding to the protocol -- Lipreading sentence with context
class SingleSentenceQuestion(models.Model):
    text = models.CharField(max_length=200)
    video_path = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(VideoQuiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        answers = list(self.singlewordanswer_set.all())
        random.shuffle(answers)
        return answers

    pass

class SingleSentenceAnswer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(SingleWordQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question: {self.question}, Answer: {self.text}, Correct: {self.correct}"
        
    pass

# Model corresponding to the lipreading protocol -- Lipreading missing words in sentences
class MissingWordsQuestion(models.Model):
    text = models.CharField(max_length=200)
    video_path = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(MissingWordInSentenceQuiz, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)

    # get the possible answers to the question -- in this protocol, the correct answer is a text field
    def get_answers(self):
        answers = list(self.missingwordsanswer_set.all())
        random.shuffle(answers)
        return answers

class MissingWordsAnswer(models.Model):
    # text = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    # has a foreign key reference to missing word in sentence question
    question = models.ForeignKey(MissingWordsQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question: {self.question}, Correct answer: {self.answer}"