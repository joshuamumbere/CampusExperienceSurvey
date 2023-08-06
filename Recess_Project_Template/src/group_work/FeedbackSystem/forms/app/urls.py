# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('course_feedback/', views.course_feedback, name='course_feedback'),
    path('instructor_feedback/', views.instructor_feedback, name='instructor_feedback'),
    path('campus_feedback/', views.campus_feedback, name='campus_feedback'),
]
