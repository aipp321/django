from django.contrib import admin
from .models import Bolg_type, Bolgs
# Register your models here.


@admin.register(Bolg_type)
class Bolg_type_admin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Bolgs)
class Bolg_admin(admin.ModelAdmin):
    list_display = ('id', 'title','blog_type', 'author', 'created_time')