from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ManyToManyField(to='Author')
    tags = models.ManyToManyField(to='Tag')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_created=True)
    is_published = models.BooleanField(default=True)


class Author(models.Model):
    name = models.CharField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=100)
