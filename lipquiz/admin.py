from django.contrib import admin
from .models import MissingWordInSentenceQuiz, VideoQuiz

# Register your models here.
admin.site.register(VideoQuiz)
admin.site.register(MissingWordInSentenceQuiz)