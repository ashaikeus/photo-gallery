from django.db import models
from django.utils import timezone


class Photo(models.model):
    link_to_image = models.TextField(null=False)
    people = models.ManyToManyField('Person', through='PhotoPerson', null=False)
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=75)
    description = models.TextField()
    place = models.CharField(max_length=75)
    tags = models.ManyToManyField('Tag', through='PhotoTags')

    likes = models.ManyToManyField('Person', through='PhotoLikes')
    comments = models.ManyToManyField('Person', through='PhotoComments')
    owner = models.ForeignKey('Person', on_delete=models.SET_NULL)
    upload_date = models.DateTimeField(default=timezone.now)
    # trusted_users = models.ManyToManyField('Person', through='PhotoTrust')
    album_id = models.IntegerField(default=0)


class Person(models.model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    link_to_avatar = models.TextField()
    gender = models.CharField(max_length=1, choices=(("m", "Мужчина"), ("f", "Женщина")))
    birthdate = models.DateTimeField()
    city = models.CharField(max_length=50)
    mother = models.ForeignKey('Person', on_delete=models.SET_NULL, limit_choices_to={"gender": "f"})
    father = models.ForeignKey('Person', on_delete=models.SET_NULL, limit_choices_to={"gender": "m"})
    children = models.ManyToManyField('Person', through='ParentsChildren')
    spouse = models.ForeignKey('Person', on_delete=models.SET_NULL, limit_choices_to={"gender__ne": gender})
    # exes = models.ManyToManyField


class Tag(models.model):
    name = models.CharField(max_length=70)


class Comment(models.model):
    author = models.ForeignKey('Person', on_delete=models.SET_NULL)
    text = models.TextField()


# Many-to-many relationship tables

class PhotoPerson(models.model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class PhotoTags(models.model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class PhotoLikes(models.model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    like = models.ForeignKey(Person, on_delete=models.CASCADE)


class PhotoComments(models.model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class ParentsChildren(models.model):
    parent = models.ForeignKey(Person, on_delete=models.CASCADE)
    child = models.ForeignKey(Person, on_delete=models.CASCADE)
