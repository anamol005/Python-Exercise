## 1.
    # Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
    # Write a main program that rolls the dice until the result is 6. The main program should print out the result of
    # each roll.

import random

def roll_dice():
    return random.randint(1, 6)

result = 0

print('Rolling the dice until we get a 6...\n')

while result != 6:
    result = roll_dice()
    print('You rolled:', result)


## 2.
    # Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified
    # function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that
    # the dice rolling in the main program continues until the program gets the maximum number on the dice, which
    # is asked from the user at the beginning.

import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input('Enter the number of sides on the dice: '))

result = 0
print(f'\nRolling a {sides}-sided dice until we get {sides}...\n')

while result != sides:
    result = roll_dice(sides)
    print('You rolled:', result)


## 3.
    # Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
    # Write a main program that asks for a volume in gallons from the user and converts the value to liters. The
    # conversion must be done by using the function. Conversions continue until the user inputs a negative value.

def gallons_to_liters(gallons):
    return gallons * 3.78541

while True:
    gallons = float(input('Enter the amount of gasoline in gallons (negative to quit): '))

    if gallons < 0:
        print('Program ended.')
        break

    liters = gallons_to_liters(gallons)
    print(f'{gallons} gallons is equal to {liters:.2f} liters.\n')


## 4.
    # Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers
    # in the list. For testing, write a main program where you create a list, call the function, and print out the
    # value it returned.

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_numbers = [5, 10, 3, 7, 2]

result = sum_list(my_numbers)
print('The sum of the numbers in the list is:', result)


## 5.
    # Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise
    # the same as the original list except that all uneven numbers have been removed. For testing, write a main program
    # where you create a list, call the function, and then print out both the original as well as the cut-down list.

def remove_odd_numbers(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

original_list = [1, 4, 7, 10, 13, 16]

filtered_list = remove_odd_numbers(original_list)

print('Original list:', original_list)
print('List without odd numbers:', filtered_list)


## 6.
    # Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the
    # pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program
    # asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value
    # for money (which of them has a lower unit price). You must use the function you wrote for calculating the unit
    # prices.

import math

def pizza_unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100  
    area_m2 = math.pi * (radius_m ** 2)  
    unit_price = price_eur / area_m2
    return unit_price

diameter1 = float(input('Enter the diameter of the first pizza (cm): '))
price1 = float(input('Enter the price of the first pizza (euros): '))

diameter2 = float(input('Enter the diameter of the second pizza (cm): '))
price2 = float(input('Enter the price of the second pizza (euros): '))

unit_price1 = pizza_unit_price(diameter1, price1)
unit_price2 = pizza_unit_price(diameter2, price2)

print(f'\nUnit price of first pizza: {unit_price1:.2f} euros/m²')
print(f'Unit price of second pizza: {unit_price2:.2f} euros/m²')

if unit_price1 < unit_price2:
    print('The first pizza provides better value for money.')
elif unit_price2 < unit_price1:
    print('The second pizza provides better value for money.')
else:
    print('Both pizzas have the same value for money.')





























































