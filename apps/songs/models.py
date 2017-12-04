from __future__ import unicode_literals
from django.db import models
from ..login.models import User


class SongManager(models.Manager):
    def Song_validator(self, postData, id):
        response = {'status': True, 'errors': []}
        if len(postData['link']) < 1:
            response['errors'].append(
                "Please add a Spotify link!")
        if len(postData['song']) < 1:
            response['errors'].append(
                "Song/artist cannot be empty!")
        if len(response['errors']) == 0:
            return response
        else:
            response['status'] = False
        return response

    def addfav(self, id):
        response = {'status': True, 'errors': []}
        if len(Song.objects.filter(id=id)) == 0:
            response['errors'].append('Cannot find song!')
        if len(response['errors']) == 0:
            return response
        else:
            response['status'] = False
        return response

    def removefav(self, id):
        response = {'status': True, 'errors': []}
        if len(Song.objects.filter(id=id)) == 0:
            response['errors'].append('Cannot find song!')
        if len(response['errors']) == 0:
            return response
        else:
            response['status'] = False
        return response

    def restofsongs(self, id):
        response = []
        songs = Song.objects.all().order_by('-id')
        for i in songs:
            if len(i.favorited_by.filter(id=id)) == 0:
                response.append(i)
        return response


class Song(models.Model):
    song = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    favorited_by = models.ManyToManyField(User, related_name="favorite_songs")
    user = models.ForeignKey(User, related_name="songs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SongManager()

    def __repr__(self):
        return "<Song: {} {} {}>".format(self.user, self.song, self.link)