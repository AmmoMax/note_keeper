from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ManyToManyField(to='Author')
    tags = models.ManyToManyField(to='Tag')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
