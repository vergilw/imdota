from django.contrib import admin

# Register your models here.

from .models import Studio
from .models import Author
from .models import Play
from .models import Platform
from .models import Character
from .models import Tag
from .models import PlayComment
from .models import User

admin.site.register(Studio)
admin.site.register(Author)
admin.site.register(Play)
admin.site.register(Platform)
admin.site.register(Character)
admin.site.register(Tag)
admin.site.register(PlayComment)
admin.site.register(User)

