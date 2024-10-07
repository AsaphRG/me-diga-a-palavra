from django.contrib import admin
from databases import models

from django.contrib.auth.admin import UserAdmin
from databases.forms import CustomUserCreationForm

# Register your models here.
@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    ...


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    ...


@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = models.CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('sex', 'country', 'state', 'birth_date')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('sex', 'country', 'state', 'birth_date')}),
    )


# @admin.register(models.Visit)
# class Visit(admin.ModelAdmin):
#     ...


@admin.register(models.Theme)
class ThemeAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Move)
class MoveAdmin(admin.ModelAdmin):
    ...
