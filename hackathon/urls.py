from django.urls import path,include
from . import views 

urlpatterns = [
    path('create/',views.createHackathon.as_view()),
    path('register/',views.registerParticipant.as_view()),
    path('registeredHackathons/',views.getRegisteredHackathons.as_view()),
    path('getHackathons/',views.getHackathons.as_view()),
]