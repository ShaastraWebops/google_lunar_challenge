from django.contrib import admin
from authmn.models import UserProfile
from django.contrib.auth.models import User

class TeamAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, TeamAdmin)

