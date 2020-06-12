from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile, Notification

# Create your models here.
class Make(models.Model):
    name = models.CharField(max_length=255)


class Car_Model(models.Model):
    name = models.CharField(max_length=255)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)

class Vehicle(models.Model):
    TYPES = (
        ('Evakuator', 'Evakuator'),
        ('Refrigerator', 'Refrigerator'),
    )

    STATUS = (
        ('On The Way', 'On The Way'),
        ('Free', 'Free')
    )
    type_car = models.CharField(max_length=255, choices=TYPES)
    person = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=25)
    phone2 = models.CharField(max_length=25, null=True, blank=True)
    phone3 = models.CharField(max_length=25, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    no = models.CharField(max_length=15)
    evakuator_type = models.CharField(max_length=255, null=True, blank=True)
    capacity = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    length = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS, default="Free")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.person + ' ' + self.model

    def save(self, *args, **kwargs):
        print("Save Method")
        user = User.objects.all()
        sharer = self.updated_by.first_name + ' ' + self.updated_by.last_name
        print(sharer)
        profile = Profile.objects.get(user=self.updated_by)
        for u in user:
            if u.id == self.updated_by.id:
                continue
            
            if self.pk is None:
                noteText = self.model + " Vehicle has been added"
            else:
                noteText = self.model + " Vehicle has been updated"
            redirectUrl = '/vehicles'
            n = Notification(user=u, who=sharer, profile_picture = profile.profile_picture, note=noteText, url=redirectUrl, where="vehicle", read=False)
            n.save()
        super().save(*args, **kwargs)


