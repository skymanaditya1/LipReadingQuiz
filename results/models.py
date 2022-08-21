from django.db import models
from quizzes.models import Quiz
from lipquiz.models import MissingWordInSentenceQuiz, VideoQuiz
from django.contrib.auth.models import User

# Create your models here.
# Result is the user's result (score) on a particular quiz
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)

class SingleWordResult(models.Model):
    quiz = models.ForeignKey(VideoQuiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return self.quiz.name + "_" + self.user.username
        # return str(self.pk)


# Result model corresponding to lipreading protocol -- missing words in sentences
class MissingWordsResult(models.Model):
    quiz = models.ForeignKey(MissingWordInSentenceQuiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return self.quiz.name + "_" + self.user.username