from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    author = models.CharField(max_length=50)
    commit = models.IntegerField()
    comment = models.CharField(max_length=1000)
    file_path = models.CharField(max_length=50)
    start_offset = models.IntegerField()
    end_offset = models.IntegerField()

class MyUser(models.Model):
    to_review = models.ManyToManyField("Commit")   # commit_no
    reviewed = models.IntegerField()    # commit_no
    user = models.OneToOneField(User)

class Commit(models.Model):
  commit_no = models.IntegerField()    #commit_no