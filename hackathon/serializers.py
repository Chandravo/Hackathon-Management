from rest_framework import serializers

from .models import *

class HackathonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hackathon
        fields = ['id','name','img','submission_type','start','end','reward']
        
        