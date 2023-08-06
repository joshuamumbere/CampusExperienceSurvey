from django import forms
from .models import CourseFeedback, InstructorFeedback, CampusFeedback

class CourseFeedbackForm(forms.ModelForm):
    class Meta:
        model = CourseFeedback
        fields = '__all__'

class InstructorFeedbackForm(forms.ModelForm):
    class Meta:
        model = InstructorFeedback
        fields = '__all__'

class CampusFeedbackForm(forms.ModelForm):
    class Meta:
        model = CampusFeedback
        fields = '__all__'
