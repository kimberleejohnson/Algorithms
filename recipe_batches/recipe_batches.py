#!/usr/bin/python

# Pseudocode
## Consider your bounds: What _can't_ this function output/accept? 
# If the dictionaries are empty, exit out 

## Steps  
## Accept recipe, ingredients as parameters
## Check the first bounds cases: exit out if there are different numbers of ingredients to the recipe, e.g. too few 
## Set up global variables 
### batches: None for now, to be set 
## Calculate max batches 
### Divide ingredients[quantity] by recipe[quantity] 
### Initialize counter batches from None to new quantity 
### But, if we continue through the loop and current_batches becomes smaller than batches, give batches that new value 
## Return batches

import math

def recipe_batches(recipe, ingredients):
  
  # Base case, need same number of recipe and ingredients
  ## Converting values of dictionary to list
  if len(list(dict.values(recipe))) is not len(list(dict.values(ingredients))): 
    return 0

  # Value to be returned, currently set to None, to be updated
  batches = None

  # Loop, divide the quantity of ingredients by quantity required by recipe 
  for quantity in recipe:
    current_batches = ingredients[quantity] // recipe[quantity]

    # Initialize batches value with first result 
    if batches is None: 
      batches = current_batches 
    
    # But continue comparing 
    elif current_batches < batches: 
      batches = current_batches 
  
  # Output 
  return batches 

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))