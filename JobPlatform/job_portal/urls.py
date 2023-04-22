from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('home/', views.home, name='HomePage'),
    path('home/addNew/', views.addNewJob, name='AddNew'),
    path('home/jobInfo/<int:id>', views.jobInfo, name='JobsInfo')
]