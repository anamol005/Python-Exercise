## 1.
    # Write a program that asks the user how many dice to roll. The program rolls all the dice
    # once and prints out the sum of the numbers. Use a for loop.

import random

dice_count = int(input('How many dice do you want to roll? '))
total = 0

for i in range(dice_count):
    roll = random.randint(1, 6)  # random number between 1 and 6
    total = total + roll  # add the roll to total

print('The total sum of dice is:', total)


## 2.
    # Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five
    # greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.


numbers = []
while True:
    user_input = input('Enter a number (or press Enter to quit): ')

    if user_input == '':
        break

    numbers.append(int(user_input))

numbers.sort(reverse=True)
print('The five greatest numbers are:', numbers[:5])


## 3.
    # Write a program that asks the user for an integer and tells if the number is a prime number.
    # Prime numbers are number that are only divisible by one or the number itself.
    # For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
    # On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

number = int(input('Enter an integer: '))

if number > 1:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, 'is a prime number.')
    else:
        print(number, 'is not a prime number.')
else:
    print(number, 'is not a prime number.')


## 4.
    # Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names)
    # and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per
    # line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.

cities = []

for i in range(5):
    city = input('Enter the name of a city: ')
    cities.append(city)

print('\nThe cities you entered are:')
for city in cities:
    print(city)
























































































