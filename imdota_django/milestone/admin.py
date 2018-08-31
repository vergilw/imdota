from django.contrib import admin

from .models import Championship
from .models import Team

# Register your models here.

admin.site.register(Championship)
admin.site.register(Team)