from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    COLORS = (
        ('side-nav-dark header-dark', 'Dark'),
        ('', 'Light')
    )

    profile_picture = models.ImageField(upload_to='photos/%Y/%m/%d/')
    color_choice = models.CharField(max_length=255, choices=COLORS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    who = models.CharField(max_length=50)
    profile_picture = models.CharField(max_length=255, null=True, blank=True)
    note = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(null=True)
    url = models.CharField(max_length=255,null=True, blank=True)
    where = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.who
 
        
