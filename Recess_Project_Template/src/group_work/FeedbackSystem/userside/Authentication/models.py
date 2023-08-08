from django.db import models

# Create your models here.


# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=50, unique=True)
    # st_id=models.CharField(max_length=50,null=False)
    # st_email=models.EmailField(unique=True)
    email = models.EmailField(unique=True)
    student_number = models.CharField(max_length=10, unique=True)
    YEAR_CHOICES = [
        ('One', 'Year One'),
        ('Two', 'Year Two'),
        ('Three', 'Year Three'),
        ('Four', 'Year Four'),
    ]
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)

    def __str__(self):
        return self.username  #

    # def __str__(self):
    #     return self.st_name
