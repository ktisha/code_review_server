__author__ = 'ktisha'

from django.contrib import admin
from models import Review

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Review, AuthorAdmin)
