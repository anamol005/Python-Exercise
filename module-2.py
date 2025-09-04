# 1.
    # Write a program that asks your name and then greets you by your name: Examples:
    # If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
    # If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!

# name = input('Enter your name: ')

# print('Hello, ' + name + '!')


# 2.
    # Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

# import math
# radius = float(input('Enter the radius of circle: '))
# area = math.pi * radius * radius                      # formula of area of circle = π * r^2

# print('The area of circle is = ',area)


# 3.
    # Write a program that asks the user for the length and width of a rectangle.
    # The program then prints out the perimeter and area of the rectangle.
    # The perimeter of a rectangle is the sum of the lengths of each four sides.

# length = int(input('Enter the Length: '))
# width = int(input('Enter the Width: '))

# area = length * width
# perimeter = 2 * (length + width)

# print('The area of rectangle is = ', area)
# print('The perimeter of rectangle is = ', perimeter)


# 4.
    # Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.

# num = int(input("Enter a first number: "))
# num1 = int(input("Enter a second number: "))
# num2 = int(input("Enter a third number: "))

# sum = num + num1 + num2
# product = num * num1 * num2
# average = (sum / 3)

# print('The sum of number is = ', sum)
# print('The product of number is = ', product)
# print('The average of number is = ', average)


# 5.
    # Write a program that asks the user to enter a mass in medieval units: talents, pounds, and lots .
    # The program converts the input to full kilograms and grams and outputs the result to the user:
    # One talent is 20 pounds.
    # One pound is 32 lots.
    # One lot is 13,3 grams.

# talents = float(input("Enter the number of talents : "))
# pounds = float(input("Enter the number of pounds : "))
# lots = float(input("Enter the number of lots : "))

# grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
# Kilogram=grams/1000

# print('The weight in modern units is',Kilogram,'kg')


# 6.
    # Write a program that draws two random combinations of numbers for a combination lock:
    # a 3-digit code where each number is between 0 and 9.
    # a 4-digit code where each number is between 1 and 6.

# import random
# digit1 = random.randint(0, 9)
# digit2 = random.randint(0, 9)
# digit3 = random.randint(0, 9)
#
# code1 = random.randint(1, 6)
# code2 = random.randint(1, 6)
# code3 = random.randint(1, 6)
# code4 = random.randint(1, 6)
#
# print("3-digit code (0-9):", digit1, digit2, digit3)
# print("4-digit code (1-6):", code1, code2, code3, code4)
