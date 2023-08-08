from django.shortcuts import render, redirect
from .forms import CourseFeedbackForm, InstructorFeedbackForm, CampusFeedbackForm

def course_feedback(request):
    if request.method == 'POST':
        form = CourseFeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database (if desired)
            return redirect('instructor_feedback')
    else:
        form = CourseFeedbackForm()
    return render(request, 'course_feedback.html', {'form': form})

def instructor_feedback(request):
    if request.method == 'POST':
        form = InstructorFeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database (if desired)
            return redirect('campus_feedback')
    else:
        form = InstructorFeedbackForm()
    return render(request, 'instructor_feedback.html', {'form': form})

def campus_feedback(request):
    if request.method == 'POST':
        form = CampusFeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database (if desired)
            return redirect('thank_you')
    else:
        form = CampusFeedbackForm()
    return render(request, 'campus_feedback.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

# FeedbackSystem/views.py

from django.shortcuts import render, redirect
from .forms import CourseFeedbackForm, InstructorFeedbackForm, CampusFeedbackForm

def submit_course_feedback(request):
    # Add any additional processing for form submission here if needed
    return redirect('instructor_feedback')

