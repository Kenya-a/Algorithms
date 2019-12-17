#!/usr/bin/python

#import math
import operator

def recipe_batches(recipe, ingredients):
  #Number of whole batches that can be made
  whole_batches = {}

  for x, y in recipe.items():
    if x not in ingredients:
      return 0

    whole_batches[x] = ingredients[x] // y

  return min(whole_batches.items(), 
key = operator.itemgetter(1))[1]
      #Python Docs: Return a callable object that fetches item from its operand.If multiple items are specified, returns a tuple of lookup values

  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))