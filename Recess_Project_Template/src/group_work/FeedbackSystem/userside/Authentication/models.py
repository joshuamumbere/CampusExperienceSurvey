from django.db import models

# Create your models here.


# Create your models here.
class Student(models.Model):
    st_name=models.CharField(max_length=50,unique=True)
    # st_id=models.CharField(max_length=50,null=False)
    # st_email=models.EmailField(unique=True)

    def __str__(self):
        return self.st_name
