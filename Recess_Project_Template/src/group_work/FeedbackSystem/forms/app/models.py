

from django.db import models

#Model for Course feedback
class CourseFeedback(models.Model):
    # Fields for the course feedback form
    student_name = models.CharField(max_length=100)

    # Select field (choices for a dropdown)
    select_course = models.CharField(max_length=50, choices=[(
        'software_engineering', 'Bachelor of Science in Software Engineering'), ('computer_science', 'Bachelor of Science in Computer Science'), ('infosystems_technology', 'Bachelor of Science in Information Systems and Technology')])
    # Select year of study field
    select_year = models.CharField(max_length=50, choices=[(
        'year_1', 'YEAR 1'), ('year_2', 'YEAR 2'), ('year_3', 'YEAR 3'), ('year_4', 'YEAR 4')])

    # Select favorite course unit field
    course_unit = models.CharField(max_length=50, choices=[(
        'courseunit_1', 'Mobile Programming'), ('courseunit_2', 'Requirements Engineering'), ('courseunit_3', 'Artificial Intelligence'), ('courseunit_4', 'Data Communication'),('courseunit_5', 'Object Oriented Programming'),('courseunit_6', 'Computer Networks'),('courseunit_7', 'Operating Systems'),('courseunit_8', 'Database Management'),('courseunit_9', 'Emerging Web Technologies'),('courseunit_10', 'Data Structures and Algorithms'),])

    # Rating field (choices: 1 to 5)
    rating_instructor = models.PositiveSmallIntegerField()

    # Textarea field
    comments_course = models.TextField()

    # Radio field (choices for the Likert scale) for selecting how satisfied the students were with the course evaluation
    course_satisfaction = models.CharField(max_length=10, choices=[('5', 'Very Satisfied'), (
        '4', 'Satisfied'), ('3', 'Neutral'), ('2', 'Dissatisfied'), ('1', 'Very Dissatisfied')])

    # Radio field (choices for the Likert scale)
    course_remarks = models.CharField(max_length=10, choices=[('5', 'Strongly Agree'), (
        '4', 'Agree'), ('3', 'Neutral'), ('2', 'Disagree'), ('1', 'Strongly Disagree')])

    # Text field
    suggestion = models.CharField(max_length=500, blank=True, null=True)

    # You can add more fields as needed based on your form's questions

    def __str__(self):
        return f"{self.student_name}'s Course Feedback"



#Model for Instructor Feedback

class InstructorFeedback(models.Model):
    # Fields for the instructor feedback form
    instructor_name = models.CharField(max_length=50, choices=[(
        'mumbere_alice', 'Dr Mumbere Alice'), ('agaba_martha', 'Dr Agaba Martha'), ('rogers_ntanda', 'Professor Rogers Ntanda'), ('ariho_geoffrey', 'Dr Ariho Geoffrey'),('birimumaaso_conrad', 'Dr Birimumaaso Conrad')])

    # Rating field (choices: 1 to 5)
    rating_instructor = models.PositiveSmallIntegerField()

    # Textarea field
    comments_instructor = models.TextField()

    # Radio field (choices for the Likert scale)
    teachings = models.CharField(max_length=10, choices=[('5', 'Very Satisfied'), (
        '4', 'Satisfied'), ('3', 'Neutral'), ('2', 'Dissatisfied'), ('1', 'Very Dissatisfied')])

    # Radio field (choices for the Likert scale)
    expectations = models.CharField(max_length=10, choices=[('5', 'Strongly Agree'), (
        '4', 'Agree'), ('3', 'Neutral'), ('2', 'Disagree'), ('1', 'Strongly Disagree')])
    

    # Radio field (choices for the Likert scale)
    evaluation = models.CharField(max_length=10, choices=[('5', 'Very Fair'), (
        '4', 'Fair'), ('3', 'Neutral'), ('2', 'Unfair'), ('1', 'Very Unfair')])
    


    # Text field
    suggestion = models.CharField(max_length=500, blank=True, null=True)

    #Additional fields

    def __str__(self):
        return f"{self.student_name}'s Instructor Feedback"

#Model for campus feedback

class CampusFeedback(models.Model):

    # Radio field (choices for the Likert scale) for how satisfied the students were with the campus facilities
    campus_facilities= models.CharField(max_length=10, choices=[('5', 'Very Satisfied'), (
        '4', 'Satisfied'), ('3', 'Neutral'), ('2', 'Dissatisfied'), ('1', 'Very Dissatisfied')])

    # Radio field (choices for the Likert scale) for how clean and well maintained the campus facilities are
    cleanliness_maintanance = models.CharField(max_length=10, choices=[('5', 'Very Clean'), (
        '4', 'Clean'), ('3', 'Neutral'), ('2', 'Dirty'), ('1', 'Very Dirty')])
    
    campus_resources = models.CharField(max_length=10, choices=[('5', 'Very Accessible'), (
        '4', 'Accessible'), ('3', 'Neutral'), ('2', 'Unaccessible'), ('1', 'Very Unaccessible')])


    # Radio field(choices for the Likert scale) for how accessible campus resources are
    campus_security = models.CharField(max_length=10, choices=[('5', 'Very Satisfied'), (
        '4', 'Satisfied'), ('3', 'Neutral'), ('2', 'Dissatisfied'), ('1', 'Very Dissatisfied')])


    # Textarea field
    comments_campus = models.TextField()

    # Select field (choices for a dropdown)
    preferred_building = models.CharField(max_length=50, choices=[(
        'building_a', 'COSCIS main building'), ('building_b', 'College Library'), ('building_c', 'Auditorium')])

    # Number field (for additional numeric data)
    visit_frequency = models.PositiveIntegerField()

    # Additional fields

    def __str__(self):
        return f"{self.student_name}'s Campus Feedback"
