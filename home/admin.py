from django.contrib import admin
from .models import Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ['fullname']
    search_fields = ['user', 'email']
    prepopulated_fields = {"slug": ("user",)}



admin.site.register(Team, TeamAdmin)
