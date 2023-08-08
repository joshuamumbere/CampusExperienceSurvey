from django import forms
from .models import CourseFeedback, InstructorFeedback, CampusFeedback
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

# Define choices for the rating_instructor field
RATING_CHOICES = [
    (1, '1 - Very Poorly'),
    (2, '2 - Poorly'),
    (3, '3 - Neutral'),
    (4, '4 - Very Well'),
    (5, '5 - Excellently'),
]
# feedback form for campus feedback


class CourseFeedbackForm(forms.ModelForm):
    class Meta:
        model = CourseFeedback
        fields = '__all__'  # Include all fields from the model

        # Custom labels for form fields
        labels = {
            'student_name': 'Your Name',
            'select_course': 'Please select your course of study',
            'select_year': 'Year of Study',
            'course_unit': 'What was your favorite course unit last semester?',
            'rating_instructor': 'Rate on a scale of 1 to 5 how well the course units were taught last semester',
            'comments_course': 'What are your thoughts on the course units taught?',
            'course_satisfaction': 'Were you satisfied with the individual assesment and final examinations on the course units taught last semester?',
            'course_remarks': 'The course materials were helpful to you and added value to your career development',
            'suggestion': 'Any other suggestions(optional)',
        }

        # Custom help text for form fields
        help_texts = {
            'rating_instructor': '1 - Very Poorly, 2-Poorly, 3 -Neutral 4-Very Well  5 - Excellently',
            'comments_course': 'Provide any additional comments about the course.',
            'select_course': 'Choose a response.',
            'select_year': 'Choose a response.',
            'suggestion': 'Any suggestions or feedback you would like to share (optional).',
            'additional_rating': 'If applicable, provide any additional rating (optional).',
        }

        # Customize widget for specific fields (e.g., use a TextInput for a CharField)
        widgets = {
            'student_name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'additional_rating': forms.NumberInput(attrs={'step': 0.1}),
            # Add custom widgets for other fields as needed
        }

    def __init__(self, *args, **kwargs):
        super(CourseFeedbackForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            'student_name',
            'course_unit',
            'rating_instructor',
            'comments_course',
            'select_course',
            'select_year',
            'suggestion',
            'additional_rating',
            Submit('submit', 'Next')
        )


 # Feedback form for Instructor feedback
RATING_CHOICES = [
    (1, '1 - Very Approachable'),
    (2, '2 - Approachable'),
    (3, '3 - Neutral'),
    (4, '4 - Unapproachable'),
    (5, '5 - Very Unapproachable'),
]


class InstructorFeedbackForm(forms.ModelForm):
    class Meta:
        model = InstructorFeedback
        fields = '__all__'

        # Custom labels for form fields
        labels = {
            'instructor_name': 'Who was your best instructor last semester?',
            'rating_instructor': 'On a scale of 1 to 5, rate how approachable the instructors were for questions and help',
            'comments_instructor': 'Give your thoughts on the instructors ability to deliver quality education',
            'teachings': 'Were you satisfied you with the instructors explanations and methods of teaching ',
            'expectations': 'The Instructors met the expected standards and provided you with the best possible knowledge ',
            'evaluation': 'How fair were the instructors grading and evaluation methods ',
            'suggestion': 'Any other Remarks (optional)',
        }

        # Custom help text for form fields
        help_texts = {
            'rating_instructor': '1 - Very Approachable, 2 - Approachable, 3 - Neutral , 4 - Unapproachable, 5 - Very unapproachable ',
            'comments_instructor': 'Provide any additional comments about the instructor.',
            'teachings': 'Choose a response. ',
            'expectations': 'Choose a response.',
            'evaluation': 'Choose a response',
            'suggestion': 'Any suggestions or feedback you would like to share (optional).',

        }

        # Customize widget for specific fields (e.g., use a TextInput for a CharField)
        widgets = {
            'student_name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'additional_rating': forms.NumberInput(attrs={'step': 0.1}),
            # Add custom widgets for other fields as needed
        }

    def __init__(self, *args, **kwargs):
        super(InstructorFeedbackForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            'instructor_name',
            'rating_instructor',
            'comments_instructor',
            'teachings',
            'expectations',
            'evaluation',
            'suggestion',
            Submit('submit', 'Next')
        )

# Feedback form for Campus feedback


class CampusFeedbackForm(forms.ModelForm):
    class Meta:
        model = CampusFeedback
        fields = '__all__'

        # Custom labels for form fields
        labels = {
            'campus_facilities': 'How satisfied were you with the campus facilities?',
            'cleanliness_maintanance': 'How clean and well maintained were the campus facilities?',
            'campus_resources': 'How accessible were the campus resources such as library and labs?',
            'campus_security': 'How satisfied were you with the campus security measures?',
            'comments_campus': 'Any additional comments about the campus facilities',
            'preferred_building': 'What was your preferred building of study?',
            'visit_frequency': 'How often would you visit campus?',
        }

        # Custom help text for form fields
        help_texts = {
            'campus_facilities': 'Choose a response.',
            'cleanliness_maintanance': 'Choose a response.',
            'campus_resources': 'Choose a response.',
            'comments_campus': 'Provide any additional comments about the campus.',
            'preferred_building': 'Select your preferred building from the dropdown.',
            'visit_frequency': 'Enter the number of times you visit campus in a week',
        }

        # Customize widget for specific fields (e.g., use a TextInput for a CharField)
        widgets = {
            'student_name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            # Add custom widgets for other fields as needed
        }

    def __init__(self, *args, **kwargs):
        super(CampusFeedbackForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            'campus_facilities',
            'campus_resources',
            'comments_campus',
            'preferred_building',
            'visit_frequency',
            Submit('submit', 'Submit Feedback')
        )
