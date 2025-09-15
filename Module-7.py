# 1.
    # Write a program that asks the user for a number of a month and then prints out the corresponding season
    # (spring, summer, autumn, winter).Save the seasons as strings into a tuple in your program. We can define \
    # each season to last three months, December being the first month of winter.

seasons = ('Winter', 'Spring', 'Summer', 'Autumn')
month = int(input('Enter the number of month from (1-12): '))
if month in (12, 1,2 ):
    season = seasons[0]
elif month in (3, 4, 5):
    season = seasons[1]
elif month in (6, 7, 8):
    season = seasons[2]
elif month in (9, 10, 11):
    season = seasons[3]
else:
   season = 'not there ! Please try again.'
print('The season is', season)

# 2.
    # Write a program that asks the user to enter names until he/she enters an empty string. After each name is read
    # the program either prints out New name or Existing name depending on whether the name was entered for the first
    # time. Finally, the program lists out the input names one by one, one below another in any order.
    # Use the set data structure to store the names.

names = set()
name = input('Enter the name: ')
while name != '':
    if name in names:
        print('Existing name')
    else:
        print('New name')
        names.add(name)
    name = input('Enter a name: ')
print('\nList of names entered:')
for n in names:
    print(n)


# 3.
    # Write a program for fetching and storing airport data.The program asks the user if they want to enter a new
    # airport, fetch the information of an existing airport or quit.If the user chooses to enter a new airport, the
    # program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport
    # information instead, the program asks for the ICAO code of the airport and prints out the corresponding name.If
    # the user chooses to quit, the program execution ends. The user can choose a new option as many times they want
    # until they choose to quit.(The ICAO code is an identifier that is unique to each airport. For example, the ICAO
    # code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

airports = {}

while True:
    print('\nChoose an option:')
    print('1 = Enter a new airport')
    print('2 = Fetch airport information')
    print('3 = Quit')

    choice = input('Your choice: ')

    if choice == '1':
        icao = input('Enter ICAO code: ').upper()
        name = input('Enter airport name: ')
        airports[icao] = name
        print(f'Airport {name} with code {icao} added.')

    elif choice == '2':
        icao = input('Enter ICAO code to search: ').upper()
        if icao in airports:
            print(f'Airport found: {airports[icao]}')
        else:
            print('No airport found with that ICAO code.')

    elif choice == '3':
        print('Goodbye! 👋')
        break

    else:
        print('Invalid choice, please try again.')