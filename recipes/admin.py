# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Recipe, Ingredient

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]

admin.site.register(Recipe, RecipeAdmin)
