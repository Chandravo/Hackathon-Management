from django.db import models
from registration.models import User
from hackathon.models import Hackathon

class Submission(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False, unique=True)
    summary = models.TextField()
    link = models.URLField(null=True,blank=True)
    img = models.URLField(null=True,blank=True)
    file = models.URLField(null=True,blank=True)
    made_by = models.ForeignKey(User,on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon,on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name    
