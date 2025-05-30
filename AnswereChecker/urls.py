from django.urls import path
from .views import check_answer_api

urlpatterns = [
    path('', check_answer_api),  # POST to /api/answere-checker/
]
