from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete = True, related_name="follower")
    followee = models.ForeignKey(User, on_delete = True , related_name="followee")
    start = models.DateTimeField()
    end = models.DateTimeField(null=True)