from __future__ import unicode_literals
from django.db import models
    
class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should have at least 2 characters."
        if len(postData['network']) < 3:
            errors['network'] = "Network should have at least 3 characters."
        if len(postData['description']) < 10:
            errors['description'] = "Please write more of a description."
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()