"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries
from random import choice
from customers import get_customers_from_file


def winner(array_object):
    random_obj = choice(array_object)
    name = random_obj.name
    email = random_obj.email
    print(f"Tell {name} at {email} that they've won")
    







def raffle():
    obj_array = get_customers_from_file("customers.txt")
    winner(obj_array)
#Basically, when you run $ python3 raffle.py, the raffle function will run whether you have that or not. When you go into python using $ python3 and then you say >>> import raffle; if you don't have that if statement then the raffle function will run (the module runs on import), but if you do have that if statement the raffle function won't run as the name won't equal main when called via a module.  You can then call raffle.raffle_run() when you want to run the function.
if __name__ == "__main__":
    raffle()