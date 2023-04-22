from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from .models import jobsInfo

# Create your views here.
def main(request):
    mytemplate = loader.get_template('index.html')
    return HttpResponse(mytemplate.render())

@require_http_methods(["POST"])
def home(request):
    if 'vacancies' in request.POST:
        jobs = jobsInfo.objects.all().values()
        template = loader.get_template('jobsPage.html')
        context = {
            'jobs': jobs,
        }
        return HttpResponse(template.render(context, request))
    
    if 'addNew' in request.POST:
        mytemplate = loader.get_template('addNew.html')
        return HttpResponse(mytemplate.render())
    
@require_http_methods(["POST"])
def addNewJob(request):
    if 'save' in request.POST:
        data = request.POST
        title = data.get("title")
        location = data.get("location")
        companyName = data.get("companyName")
        responsibilities = data.get("responsibilities")
        requirements = data.get("requirements")
        job = jobsInfo(title=title,location=location,companyName=companyName,responsibilities=responsibilities,requirements=requirements)
        job.save()
    return HttpResponse("Job saved succesfully")

def jobInfo(request, id):
  job = jobsInfo.objects.get(id=id)
  mytemplate = loader.get_template("jobDetails.html")
  context = {
    'job' : job,
        }
  return HttpResponse(mytemplate.render(context,request))

    


 