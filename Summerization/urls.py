from django.urls import path
from .views import summarize_url

urlpatterns = [
    path('', summarize_url),  # will handle POST to /api/summerization/
]