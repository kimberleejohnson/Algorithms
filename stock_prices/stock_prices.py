#!/usr/bin/python

# Pseudocode 
# Receive input 
# What cases are out of bounds? If length is <= 1 
# Calculate largest sequential price - smallest sequential price (single buy and sell)
  # Sequential meaning price subtracted must come before largest, because stocks 
  # Loop through numbers
  # At i price, get difference of i minus value at previous index, initialized at [0]
  # If the difference in values is greater than first difference, set first difference to next profit
  # At the same time, if another price found to be smaller, set it to min
# Return maximum profit (difference)

import argparse

def find_max_profit(prices):
  
  # Bounds: Function can't run if it's 1 or fewer price 
  if len(prices) <= 1: 
    return None 
  
  # Initializing values outside the loop
  min_so_far = prices[0]
  max_profit_so_far = prices[1] - min_so_far
  
  # Looping over values 
  for i in range(1, len(prices) - 1): 
    
    # Establish profit (difference) tracker
    next_profit = prices[i] - min_so_far
    
    # Compare profit tracker to initialized profit 
    # If it is greater override initialized profit 
    if next_profit > max_profit_so_far: 
      max_profit_so_far = next_profit
    
    # Compare value of indexed price to min 
    # If it's smaller than min_so_far, reset new min
    if prices[i] < min_so_far: 
      min_so_far = prices[i]
  
  # Return profit 
  return max_profit_so_far 
      


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))