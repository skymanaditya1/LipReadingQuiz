from django.db import models

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

    def __str__(self):
        return f"{self.name}--{self.description}"
    
    def get_questions(self):
        return self.singlewordquestion_set.all()

    class Meta:
        verbose_name_plural = 'VideoQuizzes'