from django.urls import path
from .views import QuizChecker_api

urlpatterns = [
    path('', QuizChecker_api),  # POST to /api/answere-checker/
]
