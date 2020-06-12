from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_out
from django.contrib.auth.models import User
from django.contrib import messages #flash messages import
from .models import Profile, Notification
from .forms import ProfileForm
from django.core import serializers
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'accounts/login.html')

def logout(request):
	auth_out(request)
	return redirect('/')


@login_required(login_url='/login')
def settings(request):
    profile = Profile.objects.get(user=request.user)
    profileForm = ProfileForm(instance=profile)
    if request.method == 'POST':
        try:
            profileForm = ProfileForm(request.POST, request.FILES, instance=profile)
            profileForm.save()
            messages.success(request, 'Settings has been updated.')
        except:
            messages.error(request, 'Data is not valid')
        return redirect('settings')

    context = {
        'profile': profile,
        'form': profileForm
    }
    return render(request, 'accounts/settings.html', context)


@login_required(login_url="/login")
def deleteError(request):
    return render(request, 'accounts/deleteError.html')


def notifications(request):
    data = serializers.serialize('json', Notification.objects.all().filter(user=request.user, read=False).order_by('-id'))
    return HttpResponse(data, content_type="text/json-comment-filtered")

def notify(request):
    notifications = Notification.objects.all().filter(user=request.user).order_by('-id')
    context = {
        'notifications': notifications
    }
    return render(request, 'accounts/notifications.html', context)

def makeSeen(request):
    notifications = Notification.objects.all().filter(user=request.user).order_by('-id')
    for note in notifications:
        note.read = True
        note.save()
    return redirect('notify')
    