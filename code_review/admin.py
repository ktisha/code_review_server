from code_review.models import User

__author__ = 'ktisha'

from django.contrib import admin
from models import Review

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review, AuthorAdmin)
admin.site.register(User, AuthorAdmin)
