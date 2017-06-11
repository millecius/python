# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from models import *
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('name', )

class JeuxAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', )
    search_fields = ('title', )
    list_filter = ('title', )

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created', )
    search_fields = ('title', )
    list_filter = ('title', )


admin.site.register(Type, TypeAdmin)
admin.site.register(Jeux, JeuxAdmin)
admin.site.register(Commentaire, CommentaireAdmin)

