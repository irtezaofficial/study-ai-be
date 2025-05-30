from django.urls import path
from .views import generate_question_api

urlpatterns = [
    path('', generate_question_api),  # POST to /api/question-generator/
]
