from django.db import models

# Create your models here.
# from django.db import models
from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    
    def __str__(self):
        return self.name

# class Recipe(models.Model):
#     name = models.CharField(max_length=200)
#     area = models.CharField(max_length=100, blank=True)
#     category = models.CharField(max_length=100, blank=True)
#     instructions = models.TextField(blank=True)
#     # image_url = models.URLField(max_length=500, blank=True)
#     image_url = models.ImageField(upload_to='recipes/')

    def __str__(self):
        return self.name
    
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ingredients", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    measure = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.measure} {self.name}"
