from django.urls import path
from . import views

urlpatterns =[
    path('create/',views.createSubmission.as_view()),
    path('getSubmissions/',views.getSubmissions.as_view())
]