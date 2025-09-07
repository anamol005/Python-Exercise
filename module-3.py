# 1.
    # Write a program that asks a fisher the length of a zander in centimeters.
    # If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and
    # notifies the user of how many centimeters below the size limit the caught fish was.
    # A zander must be 42 centimeters or longer to meet the size limit.

length = int(input('Enter the length of the zander in cm: '))

if length < 42:
    limit = 42 - length
    print('Release the fish back into the lake!')
    print('The fish was', limit, 'cm below the size limit.')
else:
    print('Good! The fish meets the size limit.')


# 2.
    # Write a program that asks the user to enter the cabin class of a cruise ship and
    # then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.
    # LUX: upper-deck cabin with a balcony.
    # A: above the car deck, equipped with a window.
    # B: windowless cabin above the car deck.
    # C: windowless cabin below the car deck.
    # If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

cabin_class = input('Enter the cabin class LUX, A, B, C: ').upper()
                                    # .upper() makes the input uppercase, so the program works even if the user type in small letter like lux or a.

if cabin_class == 'LUX':
    print('Upper-deck cabin with a balcony.')
elif cabin_class == 'A':
    print('Above the car deck, equipped with a window.')
elif cabin_class == 'B':
    print('Windowless cabin above the car deck.')
elif cabin_class == 'C':
    print('Windowless cabin below the car deck.')
else:
    print('Invalid cabin class.')


# 3.
    # Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.
    # A normal hemoglobin value for adult females is between 117-155 g/l.
    # A normal hemoglobin value for adult males is between 134-167 g/l.

gender = input('Enter gender: ')
h = int(input('Enter hemoglobin value (g/l): '))

if gender == 'female':
    if h < 117:
        print('Hemoglobin value  is low')
    elif h > 155:
        print('Hemoglobin value  is high')
    else:
        print('Hemoglobin value  is normal')
elif gender == 'male':
    if h < 134:
        print('Hemoglobin value  is low')
    elif h > 167:
        print('Hemoglobin value  is high')
    else:
        print('Hemoglobin value is normal')

# 4.
    # Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
    # A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400.


year = int(input('Enter a year: '))

if year % 4 != 0:                                   # ! = not equal to
    print('not a leap year')
elif year % 100 != 0:
    print('leap year')
elif year % 400 == 0:
    print('leap year')
else:
    print('not a leap year')

