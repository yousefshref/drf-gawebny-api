from django.db import models
from django.contrib.auth.models import User
import json

post_choices = [
    ('ask', 'ask'),
    ('post', 'post'),
]


class Comments(models.Model):
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=1500, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.username)


class Up(models.Model):
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, unique=True)

    def __str__(self):
        return str(self.username)


class Post(models.Model):
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    typeof = models.CharField(
        max_length=10, choices=post_choices, null=True, blank=True)
    post = models.CharField(max_length=1500, null=True, blank=True)

    ups = models.ManyToManyField(
        Up, null=True, blank=True, db_index=True)

    comments = models.ManyToManyField(
        Comments, null=True, blank=True,)
    post_date = models.CharField(max_length=100, null=True, blank=True)
    # downs = models.CharField(max_length=1500, null=True,
    #                          blank=True, db_index=True, unique=True)

    def __str__(self):
        return str(self.username)
    
    def getcomments(self):
        return self.comments.order_by('id')
