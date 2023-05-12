from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from registration.models import User
from datetime import datetime
from django.utils import timezone
from .serializers import *

class createHackathon(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self,request):
        user = request.user
        if (not user.can_host_hackathon):
            return Response({'error':'You are not authorised to host a hackathon'},status=status.HTTP_401_UNAUTHORIZED)
        name = request.data.get('name')
        description = request.data.get('description')
        img = request.data.get('background')
        submission_type = request.data.get('submission_type')
        start = request.data.get('start')
        end = request.data.get('end')
        start_day = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        end_day = datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
        reward = request.data.get('reward')
        current_day = datetime.now().replace(tzinfo=None)
        if (name is None or start is None or end is None):
            return Response({'error':'Please fill the mandatory fields'},status=status.HTTP_400_BAD_REQUEST)
        if (start_day<current_day):
            return Response({'error':"Start time has already passed"})
        if (end_day<start_day):
            return Response({'error':'end time cannot be before start time'})
        if (Hackathon.objects.filter(name=name).exists()):
            return Response({'error':'Hackathon Name is already taken. Please choose another name'},status=status.HTTP_400_BAD_REQUEST)
        hackathon = Hackathon.objects.create(
            name = name,
            description = description,
            creator = user,
            img = img,
            submission_type = submission_type,
            start = start_day,
            end = end_day,
            reward = reward
        )
        hackathon.save()
        return Response({'status':'success'},status=status.HTTP_201_CREATED)

class registerParticipant(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self,request):
        user = request.user
        name = request.data.get('hackathon_name')
        if (not Hackathon.objects.filter(name=name).exists()):
            return Response({'error':'Hackathon does not exist'},status=status.HTTP_400_BAD_REQUEST)
        hackathon = Hackathon.objects.filter(name=name).first()
        if (timezone.now()>hackathon.end):
            return Response({'error':'Hackathon has already ended'},status=status.HTTP_400_BAD_REQUEST)
        
        if (hackathon.participants.filter(id=user.id).exists()):
            return Response({'error':'You are already registered'},status=status.HTTP_400_BAD_REQUEST)
        
        hackathon.participants.add(user)
        return Response({'status':'success'},status=status.HTTP_200_OK)
    
    
class getRegisteredHackathons(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        user = request.user
        hackathons = user.hackathons.all()
        serializer = HackathonSerializer(hackathons,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
class getHackathons(APIView):
    
    def get(self,request):
        hackathons = Hackathon.objects.filter(end__gt=timezone.now())
        serializer = HackathonSerializer(hackathons,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        

        
        
        