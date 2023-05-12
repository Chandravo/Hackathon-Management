from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from registration.models import User
from hackathon.models import *
# from datetime import datetime
from django.utils import timezone
from .serializers import *

from django.db.models import Q

# to do : integrate file and image upload via request FLILES
class createSubmission(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self,request):
        user = request.user
        hackathon_name = request.data.get('hackathon_name')
        if (not Hackathon.objects.filter(name=hackathon_name).exists()):
            return Response({'error':'Hackathon does not exist'},status=status.HTTP_400_BAD_REQUEST)
        hackathon = Hackathon.objects.filter(name=hackathon_name).first()
        if (not user.hackathons.filter(id=hackathon.id).exists()):
            return Response({'error':'You have not registered for this hackathon'},status=status.HTTP_400_BAD_REQUEST)
        if (timezone.now()>hackathon.end):
            return Response({'error':'Hackathon has already ended'},status=status.HTTP_400_BAD_REQUEST)
        submission_name = request.data.get('submission_name')
        if (Submission.objects.filter(name=submission_name).exists()):
            return Response({'error':'Submission name is already taken'},status=status.HTTP_400_BAD_REQUEST)
        summary = request.data.get('summary')
        link = request.data.get('link')
        img = request.data.get('img')
        file = request.data.get('file')
        
        if (link is None and img is None and file is None):
            return Response({'error':'there is no submission'},status=status.HTTP_400_BAD_REQUEST)

        if (hackathon.submission_type=='link' and link is None
            or hackathon.submission_type=='img' and img is None
            or hackathon.submission_type=='file' and file is None
            ):
            return Response({'error':'The submission type is wrong'},status=status.HTTP_400_BAD_REQUEST)
        
        submission = Submission.objects.create(
            name = submission_name,
            summary=summary,
            link=link,
            img=img,
            file=file,
            made_by=user,
            hackathon=hackathon
        )
        submission.save()
        serializer = SubmissionSerializer(submission)
        return Response({'status':'success','data':serializer.data},status=status.HTTP_201_CREATED)
    
class getSubmissions(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        user = request.user
        hackathon_name = request.data.get('hackathon_name')
        if (not Hackathon.objects.filter(name=hackathon_name).exists()):
            return Response({'error':'Hackathon does not exist'},status=status.HTTP_400_BAD_REQUEST)
        
        hackathon = Hackathon.objects.filter(name=hackathon_name).first()
        if (not user.hackathons.filter(id=hackathon.id).exists()):
            return Response({'error':'You have not registered for this hackathon'},status=status.HTTP_400_BAD_REQUEST)
        submissions = Submission.objects.filter(Q(made_by=user) & Q(hackathon=hackathon))
        serializer = SubmissionSerializer(submissions,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
        
            