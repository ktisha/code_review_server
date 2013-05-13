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
    # to_review = models.ForeignKey("ReviewItem", related_name="author")
    reviewed = models.IntegerField()
    user = models.OneToOneField(User)

class Commit(models.Model):
  commit_no = models.IntegerField()

class ReviewItem(models.Model):
  author = models.ForeignKey("MyUser", related_name="to_review")
  commit = models.OneToOneField(Commit)
  description = models.CharField(max_length=1000)
  perm_id = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  date = models.DateField()