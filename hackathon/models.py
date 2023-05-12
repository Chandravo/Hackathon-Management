from django.db import models
from registration.models import User

FILE_TYPES = (
    ('img','image'),
    ('file','file'),
    ('link','link')
)

class Hackathon(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    img = models.URLField(null=True, blank=True)
    submission_type = models.CharField(max_length=10,choices=FILE_TYPES, default='link')
    start = models.DateTimeField(blank=False,null=False)
    end = models.DateTimeField(blank=False,null=False)
    reward = models.TextField()
    participants = models.ManyToManyField(User,related_name='hackathons')
    
    def __str__(self) :
        return self.name
    
