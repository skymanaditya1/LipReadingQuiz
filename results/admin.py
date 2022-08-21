from django.contrib import admin
from .models import MissingWordsResult, Result, SingleWordResult

# Register your models here.
admin.site.register(Result)
admin.site.register(SingleWordResult)
admin.site.register(MissingWordsResult)