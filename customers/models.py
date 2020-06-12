from django.db import models
from django.contrib.auth.models import User
from accounts.models import Notification, Profile

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=25)
    phone2 = models.CharField(max_length=25, null=True, blank=True)
    phone3 = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print("Save Method")
        user = User.objects.all()
        sharer = ''
        sharer = self.updated_by.first_name + ' ' + self.updated_by.last_name
        print(sharer)
        profile = Profile.objects.get(user=self.updated_by)
        for u in user:
            if self.pk is None:
                noteText = self.name + " Customer has been added"
            else:
                noteText = self.name + "Customer has been updated"
            redirectUrl = '/customers'
            n = Notification(user=u, who=sharer, profile_picture = profile.profile_picture, note=noteText, url=redirectUrl, where="customer")
            n.save()
        super().save(*args, **kwargs)