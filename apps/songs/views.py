from django.shortcuts import render, redirect
from ..login.models import User
from .models import Song
from datetime import datetime
from django.contrib import messages
import operator


def index(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        "all": Song.objects.restofsongs(request.session['user_id']),
        "fav": User.objects.get(id=request.session['user_id']).favorite_songs.all(),
    }
    return render(request, 'songs/index.html', context)


def add(request):
    response = Song.objects.Song_validator(request.POST,request.session['user_id'])
    if response['status'] == True:
        user = User.objects.get(id=request.session['user_id'])
        song = Song.objects.create(
            song=request.POST['song'],
            link=request.POST['link'],
            user=user,
        )
        return redirect('/dashboard')
    else:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/dashboard')
    return redirect('/dashboard')


def addfav(request, id):
    response = Song.objects.addfav(id)
    if response['status'] == True:
        this_user = User.objects.get(id=request.session['user_id'])
        this_song = Song.objects.get(id=id)
        this_user.favorite_songs.add(this_song)
    else:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/dashboard')
    return redirect('/dashboard')


def removefav(request, id):
    response = Song.objects.removefav(id)
    if response['status'] == True:
        this_user = User.objects.get(id=request.session['user_id'])
        this_song = this_user.favorite_songs.all().get(id=id)
        this_user.favorite_songs.remove(this_song)
    else:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/dashboard')
    return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect('/')

# def addfav(request, id):
#     # user = User.objects.get(id=request.session['user_id'])
#     # print user.id
#     # song = Song.objects.get(id=id)
#     # print song
#     # return redirect('/songs')