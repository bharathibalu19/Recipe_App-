# from django.shortcuts import render

# from recipes.models import Recipe

# # Create your views here.
# def recipe_list(request):
#     query = request.GET.get('q')
#     if query:
#         recipes = Recipe.objects.filter(name__icontains=query)
#     else:
#         recipes = Recipe.objects.all()
#     return render(request, 'recipes/index.html', {'recipes': recipes})
from django.shortcuts import render, get_object_or_404
from .models import Recipe, Ingredient
import requests

def index(request):
    query = request.GET.get('q', '')
    recipes = []
    if query:
        recipes = Recipe.objects.filter(name__icontains=query)
        
        if not recipes.exists():
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
            res = requests.get(url)
            data = res.json()

            if data["meals"]:
                for meal in data["meals"]:
                    recipe = Recipe.objects.create(
                        name=meal["strMeal"],
                        area=meal["strArea"] or "",
                        category=meal["strCategory"] or "",
                        instructions=meal["strInstructions"] or "",
                        image_url=meal["strMealThumb"] or ""
                    )
                    for i in range(1, 21):
                        ing = meal.get(f"strIngredient{i}")
                        meas = meal.get(f"strMeasure{i}")
                        if ing:
                            Ingredient.objects.create(recipe=recipe, name=ing, measure=meas or "")
                recipes = Recipe.objects.filter(name__icontains=query)

    return render(request, "recipes/index.html", {"recipes": recipes, "query": query})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})
