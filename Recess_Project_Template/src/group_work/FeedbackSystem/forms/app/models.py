from django.db import models

# Create your models here.
from django.db import models

class CourseFeedback(models.Model):
    # Define fields for course feedback
    # We'll use a CharField for the Likert scale choices.
    # You can use choices and foreign keys if you have predefined options.
    q1 = models.CharField(max_length=1)
    q2 = models.CharField(max_length=1)
    q3 = models.CharField(max_length=1)
    q4 = models.CharField(max_length=1)
    q5 = models.CharField(max_length=1)

    # You can add more fields like 'student', 'course', 'semester', etc.
    # For simplicity, we'll only have the Likert scale fields.

    def __str__(self):
        return f'Course Feedback - ID: {self.id}'


class InstructorFeedback(models.Model):
    # Define fields for instructor feedback
    q1 = models.CharField(max_length=1)
    q2 = models.CharField(max_length=1)
    q3 = models.CharField(max_length=1)
    q4 = models.CharField(max_length=1)
    q5 = models.CharField(max_length=1)

    # You can add more fields like 'student', 'instructor', 'semester', etc.
    # For simplicity, we'll only have the Likert scale fields.

    def __str__(self):
        return f'Instructor Feedback - ID: {self.id}'


class CampusFeedback(models.Model):
    # Define fields for campus feedback
    q1 = models.CharField(max_length=1)
    q2 = models.CharField(max_length=1)
    q3 = models.CharField(max_length=1)
    q4 = models.CharField(max_length=1)
    q5 = models.CharField(max_length=1)

    # You can add more fields like 'student', 'campus', 'semester', etc.
    # For simplicity, we'll only have the Likert scale fields.

    def __str__(self):
        return f'Campus Feedback - ID: {self.id}'
