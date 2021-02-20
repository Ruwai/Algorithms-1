#!/usr/bin/python
def recipe_batches(recipe, ingredients):
  #recipe:={}
  #ingredients:={}
  batches = None
  for k, v in recipe.items():
    if k not in ingredients.keys():
      return 0
    if ingredients[k] // recipe[k] < batches if batches != None else True:
      batches = ingredients[k] // recipe[k]
  if batches != None:
    return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))