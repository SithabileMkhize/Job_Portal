from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/job_details/<int:id>', views.job_details, name='job_details'),,
]