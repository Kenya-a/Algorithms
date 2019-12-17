#!/usr/bin/python

import argparse
                    #prices//[15, 25, 60, 3650, 150, 2, 600]
def find_max_profit(prices):

  highest_sell_value = max(prices)
  #print(prices.index(highest_sell_value))
  lowest_buying_price = prices[:prices.index(highest_sell_value)]
  #print(lowest_buying_price)
  lbp = min(lowest_buying_price)
  #print(lbp)
  profit = (highest_sell_value - lbp )
  print(profit)
  return(profit)


find_max_profit([15, 25, 60, 3650, 150, 2, 600])




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))