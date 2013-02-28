from django.db import models

# Create your models here.

class Review(models.Model):
    author = models.CharField(max_length=50)
    commit = models.IntegerField()
    comment = models.CharField(max_length=1000)
    file_path = models.CharField(max_length=50)
    start_offset = models.IntegerField()
    end_offset = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=50)
    to_review = models.ManyToManyField("Commit")   # commit_no
    reviewed = models.IntegerField()    # commit_no

class Commit(models.Model):
  commit_no = models.IntegerField()    #commit_no