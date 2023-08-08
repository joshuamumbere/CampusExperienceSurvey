from django.contrib import admin
from .models import CourseFeedback, InstructorFeedback, CampusFeedback

# Register your models here.


admin.site.register(CourseFeedback)
admin.site.register(InstructorFeedback)
admin.site.register(CampusFeedback)
