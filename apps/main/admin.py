from django.contrib import admin
from .models import (
    MenuItem,
    Menu,
    ChildrenElement
)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
    )
    search_fields = ('title',)
    prepopulated_fields = {
        'slug':('title',)
    }

class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
    )
    search_fields = ('title',)
    prepopulated_fields = {
        'slug':('title',)
    }

class ChildrenElementAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
    )
    search_fields = ('title',)
    prepopulated_fields ={
        'slug':('title',)
    }

admin.site.register(MenuItem , MenuItemAdmin)
admin.site.register(Menu , MenuAdmin)
admin.site.register(ChildrenElement , ChildrenElementAdmin)
