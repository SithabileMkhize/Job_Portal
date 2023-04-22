from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Job

# Create your views here.

def jobs(request):
  job_info = Job.objects.all().values()
  template = loader.get_template('all_jobs.html')
  context = {
    'job_info': job_info,
  }
  return HttpResponse(template.render(context, request))


def job_details(request, id):
  job_info = Job.objects.get(id=id)
  template = loader.get_template('job_details.html')
  context = {
    'job_info': job_info,
  }
  return HttpResponse(template.render(context, request))

  
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def all_jobs(request):
  template = loader.get_template('all_jobs.html')
  return HttpResponse(template.render())
    # return render(request, "all_jobs.html")


def master(request):
  template = loader.get_template('master.html')
  return HttpResponse(template.render())
    # return render(request, "master.html")

