from django.urls import path
from . import views

app_name = 'suggestions'  # Define the app_name

urlpatterns = [
    path('submit/', views.submit_suggestion, name='submit'),
    path('view/', views.view_suggestions, name='view'),
    # Add more URL patterns as needed
]
