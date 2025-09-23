"""order = ['🍔 Cheeseburger','🍟 Fries','🥤 Soda','🍦 Ice Cream','🍪 Cookie']
x = 0
def get_item(x):
  return order[x-1]

def welcome():
  return order

print(welcome())
x = int(input("What is your order?:"))

print(get_item(x))

# Write code below 💖

def dog_years(name,age):
  age *= 7
  message = f"{name} is {age} years old in human years."
  return message

print(dog_years('Bunny',3))

def greetings(first_name,last_name):
  print(last_name +', '+ first_name)

greetings('Gero', 'Pereyra')"""

class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False

bobs_burgers = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

print(vars(bobs_burgers))