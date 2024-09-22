from django.contrib import admin
from databases import models

# Register your models here.
@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    ...


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    ...


@admin.register(models.CustomUser)
class CustomUser(admin.ModelAdmin):
    ...


# @admin.register(models.Visit)
# class Visit(admin.ModelAdmin):
#     ...