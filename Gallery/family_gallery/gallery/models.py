from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models import Q


class Photo(models.Model):
    link_to_image = models.URLField(blank=False)
    # people = models.ManyToManyField('Person', through='PhotoPerson', related_name='photos_with')
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=75)
    description = models.TextField()
    place = models.CharField(max_length=75)
    # tags = models.ManyToManyField('Tag', through='PhotoTags')

    # likes = models.ManyToManyField('Person', through='PhotoLikes', related_name='photos_liked_by')
    # owner = models.ForeignKey('Person', on_delete=models.SET_NULL, blank=True, null=True)
    upload_date = models.DateTimeField(default=timezone.now)
    # trusted_users = models.ManyToManyField('Person', through='PhotoTrust')
    album_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# complex stuff, I'll return to it later
'''
class Photo(models.Model):
    link_to_image = models.TextField(blank=False)
    people = models.ManyToManyField('Person', through='PhotoPerson',
                                    related_name='photos_with')
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=75)
    description = models.TextField()
    place = models.CharField(max_length=75)
    tags = models.ManyToManyField('Tag', through='PhotoTags')

    likes = models.ManyToManyField('Person', through='PhotoLikes', related_name='photos_liked_by')
    owner = models.ForeignKey('Person', on_delete=models.SET_NULL, blank=True, null=True)
    upload_date = models.DateTimeField(default=timezone.now)
    # trusted_users = models.ManyToManyField('Person', through='PhotoTrust')
    album_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    link_to_avatar = models.TextField(blank=True)
    gender = models.CharField(max_length=1, blank=True, choices=(("m", "Мужчина"), ("f", "Женщина")))
    birthdate = models.DateTimeField(default=datetime(1000, 1, 1))
    city = models.CharField(max_length=50, blank=True)
    mother = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True,
                               related_name='mother_to', limit_choices_to={"gender": "f"}, blank=True)
    father = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True,
                               related_name='father_to', limit_choices_to={"gender": "m"}, blank=True)
    children = models.ManyToManyField('Person', through='ParentsChildren')
    spouse = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='current_spouse',
                               limit_choices_to=Q(gender='m') if gender == 'f' else Q(gender='f'))
    # exes = models.ManyToManyField

    def __str__(self):
        return self.name + ' ' + self.surname


class Tag(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Comment(models.Model):
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, blank=False)
    author = models.ForeignKey('Person', on_delete=models.SET_NULL, blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.author.name + ' - ' + self.text


class Album(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    photos = models.ManyToManyField('Photo', through='AlbumPhotos')
    circle = models.ManyToManyField('Person', through='AlbumCircles')

    def __str__(self):
        return self.name


# Many-to-many relationship tables

class PhotoPerson(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='people_in_photo')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='photos_with_person')


class PhotoTags(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='tags_for_photo')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='photos_with_tag')


class PhotoLikes(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='likes_for_photo')
    like = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='liked_by_person')


class ParentsChildren(models.Model):
    parent = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='children_to')
    child = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='parent_to')


class AlbumPhotos(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos_in_album')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='album_for_photo')


class AlbumCircles(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='circle_for_album')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='albums_for_circle')
'''