from django.contrib import admin
from .models import Question, Answer, SingleWordQuestion, SingleWordAnswer

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