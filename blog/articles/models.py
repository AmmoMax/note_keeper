from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    author = models.ManyToManyField()
    tags = models.ManyToManyField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_created=True)
    is_published = models.BooleanField(default=True)


