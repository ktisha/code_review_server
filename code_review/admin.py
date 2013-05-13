from code_review.models import MyUser, Commit, ReviewItem

__author__ = 'ktisha'

from django.contrib import admin
from code_review.models import Review

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review, AuthorAdmin)
admin.site.register(MyUser, AuthorAdmin)
admin.site.register(Commit, AuthorAdmin)
admin.site.register(ReviewItem, AuthorAdmin)
