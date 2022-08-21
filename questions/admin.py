from django.contrib import admin
from .models import MissingWordsAnswer, MissingWordsQuestion, Question, Answer, SingleWordQuestion, SingleWordAnswer

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

class SingleWordAnswerInline(admin.TabularInline):
    model = SingleWordAnswer

class SingleWordQuestionAdmin(admin.ModelAdmin):
    inlines = [SingleWordAnswerInline]

admin.site.register(SingleWordQuestion, SingleWordQuestionAdmin)
admin.site.register(SingleWordAnswer)

# register models corresponding to the missing words in sentence lipreading protocol 
class MissingWordsAnswerInline(admin.TabularInline):
    model = MissingWordsAnswer

class MissingWordsQuestionAdmin(admin.ModelAdmin):
    inlines = [MissingWordsAnswerInline]

admin.site.register(MissingWordsQuestion, MissingWordsQuestionAdmin)
admin.site.register(MissingWordsAnswer)