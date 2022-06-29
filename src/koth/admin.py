from django.contrib import admin
from .models import Box, Game, Player, GamePlayer

# Register your models here.

admin.site.register(Box)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(GamePlayer)

