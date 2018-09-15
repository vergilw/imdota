from django.contrib import admin

# Register your models here.

from .models import Studio
from .models import Author
from .models import Play
from .models import Platform
from .models import Role

admin.site.register(Studio)
admin.site.register(Author)
admin.site.register(Play)
admin.site.register(Platform)
admin.site.register(Role)

