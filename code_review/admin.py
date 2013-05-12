from code_review.models import User, Commit

__author__ = 'ktisha'

from django.contrib import admin
from code_review.models import Review

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review, AuthorAdmin)
admin.site.register(User, AuthorAdmin)
admin.site.register(Commit, AuthorAdmin)
