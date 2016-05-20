from django.shortcuts import render, redirect
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from FloraRoomApp import models

# Create your views here.


def main_page(request):
    context = {'short_articles': models.Article.objects.all()}
    return render(request, 'mainPage.html', context)


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            pass
    else:
        return redirect('/registration/')


def log_out(request):
    if request.user.is_authenticated():
        logout(request)

    return redirect('/')


def registration_user(request):

    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.save()
        return redirect('/')

    return render(request, 'registrations_form.html')
