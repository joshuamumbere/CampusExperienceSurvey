from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    username= forms.CharField(max_length=50,required=True)
    email = forms.EmailField()
    student_number = forms.IntegerField( required=True)  # Adjust max_length as needed
    YEAR_CHOICES = [
        ('One', 'Year One'),
        ('Two', 'Year Two'),
        ('Three', 'Year Three'),
        ('Four', 'Year Four'),
    ]
    year = forms.ChoiceField(choices=YEAR_CHOICES, required=True)



    class Meta:
        model = User
        fields = ['username', 'email', 'student_number','year','password1', 'password2']
