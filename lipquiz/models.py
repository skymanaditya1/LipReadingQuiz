from django.db import models
import random

# Create your models here.
QUIZ_TYPE = (
    ('single word mcq', 'single word mcq'),
    ('single word blank with context', 'single word blank with context'),
    ('sentence with context', 'sentence with context'),
    ('sentence with blank', 'sentence with blank'),
)

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class VideoQuiz(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=256)
    number_of_questions = models.IntegerField() 
    time = models.IntegerField(help_text="Duration of the quiz") # in minutes 
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)
    quiz_type = models.CharField(max_length=120, choices=QUIZ_TYPE)
    score_required_to_pass = models.IntegerField(help_text="Minimum score required to pass the quiz")
    is_visible = models.BooleanField(help_text="Whether the quiz is visible or not", default=False)

    def __str__(self):
        return f"{self.name}--{self.description}"
    
    def get_questions(self):
        questions = list(self.singlewordquestion_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'VideoQuizzes'


class MissingWordInSentenceQuiz(models.Model):
    
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=256)
    number_of_questions = models.IntegerField() 
    time = models.IntegerField(help_text="Duration of the quiz") # in minutes 
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)
    quiz_type = models.CharField(max_length=120, choices=QUIZ_TYPE)
    score_required_to_pass = models.IntegerField(help_text="Minimum score required to pass the quiz")
    is_visible = models.BooleanField(help_text="Whether the quiz is visible or not", default=False)

    def __str__(self):
        # return f"{self.name}--{self.description}"
        return f"{self.id};{self.name};{self.description};{self.number_of_questions};{self.difficulty};{self.is_visible}"
    
    def get_questions(self):
        questions = list(self.missingwordsquestion_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'MissingWordQuizzes'