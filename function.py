import random

def fortune():
  quote = ["Don't pursue happiness – create it.","All things are difficult before they are easy.","The early bird gets the worm, but the second mouse gets the cheese.","Someone in your life needs a letter from you.","Don't just think. Act!","Your heart will skip a beat.","The fortune you search for is in another cookie.","Help! I'm being held prisoner in a Chinese bakery!"]
  number = random.randint(0,7)
  print(quote[number])

def add(a,b):
  total = a+b
  return total

fortune()
print(add(10,10))

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  return stock_prices[x-1]

def max_price(a,b):
  mx = 0
  for i in range(a,b+1):
    mx = max(mx,price_at(i))
  return mx  

  

def min_price(a,b):
  return min(stock_prices)

print(max_price(1,15))
