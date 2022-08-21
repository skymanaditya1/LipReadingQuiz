from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse

def index(request):
    return render(request, 'selection_pages/select_protocol.html')

def main_surrogate(request):
    return render(request, 'selection_pages/main_surrogate.html')

def main_page(request):
    return render(request, 'selection_pages/main_page.html')

def lipread_words(request):
    # One of the functions corresponding to lirpeading words is loaded
    return render(request, 'selection_pages/quiz_page.html')