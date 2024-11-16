from django.contrib import admin # type: ignore
from apps.restourant.models import Recipe # type: ignore

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'ingredients', 'instructions', 'preparation_time', 'is_vegetarian']