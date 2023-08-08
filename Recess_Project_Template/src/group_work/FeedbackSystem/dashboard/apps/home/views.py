from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Count
from FeedbackSystem.userside.Authentication.models import Student
from FeedbackSystem.forms.app.models import CourseFeedback, CampusFeedback

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    # Fetch number of forms filled
    formsfilledcount = CourseFeedback.objects.all().count()

    # Fetch number of forms filled
    studentcount = Student.objects.all().count()

    # Count occurrences of each satisfaction level
    satisfaction_counts = CourseFeedback.objects.values('course_satisfaction').annotate(count=Count('id'))

    # Count occurrences of each satisfaction level
    fav_building_counts = CampusFeedback.objects.values('preferred_building').annotate(count=Count('id'))

    # Prepare data for the satisfaction chart
    satisfaction_labels = [item['course_satisfaction'] for item in satisfaction_counts]
    satisfaction_data = [item['count'] for item in satisfaction_counts]
    satisfaction_data = list(satisfaction_data)

    # Prepare data for the preferred building chart
    prefbuilding_labels = [item['preferred_building'] for item in fav_building_counts]
    prefbuilding_data = [item['count'] for item in fav_building_counts]

    # Add to context
    context['formsfilledcount'] = formsfilledcount
    context['studentcount'] = studentcount
    context['satisfaction_labels'] = satisfaction_labels
    context['satisfaction_data'] = satisfaction_data
    context['prefbuilding_labels'] = prefbuilding_labels
    context['prefbuilding_data'] = prefbuilding_data

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        # Fetch student form data
        studentformdata = Student.objects.all()

        # Fetch number of forms filled
        courseformdata = CourseFeedback.objects.all()

        # Add to context
        context['studentformdata'] = studentformdata
        context['courseformdata'] = courseformdata

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
