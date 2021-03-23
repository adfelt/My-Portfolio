from django.shortcuts import render

# Get access to objects in the database
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})