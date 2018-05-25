from django.contrib import admin
from .models import Player, Team, Match, Arena, \
        College, Nationality, Position, Conference,\
        Stat, Season, Coach


class TeamAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('city', 'name', 'short_name', 'coach', 'conference', 'logo')
        }),
        ('Additional data', {
            'fields': ('arena',),
        }),
    )

class PlayerAdmin(admin.ModelAdmin):
      fieldsets = (
        (None, {
                'fields': ('name', 'surname', 'position', 'team', 'number','b_day',
                           'height', 'nationality')
        }),
        ('Aditional data', {
                'fields':('weight', 'college', 'description')
        }),
        ('Photo', {
                'fields':('image',)
        })
      )


admin.site.register(Player, PlayerAdmin)
admin.site.register(Match)
admin.site.register(Arena)
admin.site.register(College)
admin.site.register(Nationality)
admin.site.register(Position)
admin.site.register(Conference)
admin.site.register(Team, TeamAdmin)
admin.site.register(Stat)
admin.site.register(Season)
admin.site.register(Coach)



