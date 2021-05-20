from django.db import models
from quizzes.models import Quiz 
from django.contrib.auth.models import User

# Create your models here.
# Result is the user's result (score) on a particular quiz
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)