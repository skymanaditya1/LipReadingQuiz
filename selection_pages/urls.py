from django.urls import path
from . import views

app_name = 'selection_pages'

urlpatterns = [
    path('protocol_selection', views.index, name='lipreading-protocol-selection'),
    # path('lipread_words', views.lipread_words, name='lipread-words'),
    # path('', views.main_page, name='landing-page'),
    path('', views.main_surrogate, name='landing-surrogate')
]