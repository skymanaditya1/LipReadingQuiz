from django.urls import path
from . import views

app_name = 'selection_pages'

urlpatterns = [
    path('', views.index, name='lipreading-protocol-selection'),
    # path('lipread_words', views.lipread_words, name='lipread-words'),
]