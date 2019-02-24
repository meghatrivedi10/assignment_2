from django.db import models
from django.contrib.auth.models import User

class Tweetlist(models.Model):
    user_key = models.ForeignKey(User, on_delete = True)
    tweet = models.CharField(max_length = 140)
    datetime = models.DateTimeField(auto_now_add=True)
