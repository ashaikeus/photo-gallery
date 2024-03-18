# Generated by Django 5.0.3 on 2024-03-18 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_comment_author_alter_person_birthdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumcircles',
            name='album',
        ),
        migrations.RemoveField(
            model_name='albumphotos',
            name='album',
        ),
        migrations.RemoveField(
            model_name='albumcircles',
            name='person',
        ),
        migrations.RemoveField(
            model_name='albumphotos',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='parentschildren',
            name='child',
        ),
        migrations.RemoveField(
            model_name='parentschildren',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='person',
            name='children',
        ),
        migrations.RemoveField(
            model_name='person',
            name='father',
        ),
        migrations.RemoveField(
            model_name='person',
            name='mother',
        ),
        migrations.RemoveField(
            model_name='person',
            name='spouse',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='people',
        ),
        migrations.RemoveField(
            model_name='photolikes',
            name='like',
        ),
        migrations.RemoveField(
            model_name='photoperson',
            name='person',
        ),
        migrations.RemoveField(
            model_name='photolikes',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='photoperson',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='phototags',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='phototags',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='AlbumCircles',
        ),
        migrations.DeleteModel(
            name='AlbumPhotos',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='ParentsChildren',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='PhotoLikes',
        ),
        migrations.DeleteModel(
            name='PhotoPerson',
        ),
        migrations.DeleteModel(
            name='PhotoTags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
