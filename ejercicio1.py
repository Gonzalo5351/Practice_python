# April 14, 2022
# Hello, I'm Gonzalo and I'm learning to program in Python3.

# Create a program that asks the user to enter their name and age.
# Prints a message addressed to the user that indicates the year 
# in which he will be 100 years old

# Additional features:
# Add to the above program a request to the user for another number, and print the last message that 
# number of times. (Hint: Order of operations exists in Python.)
# Print that many copies of the above message on separate lines. (Hint: the string "\n" is the same 
# as pressing ENTER)

from datetime import datetime

def run():
    name = input('Please, enter your name: ')
    age = int(input('Enter your age: '))
    rest = 100 - age
    dt = datetime.now()
    current_year = dt.year
    hundredth_birthday = current_year + rest
    print(name, ',', ' you will be 100 years old in the year ', str(hundredth_birthday))
    

    other_number = range(int(input('Enter anotoher number: ')))
    for i in other_number:
        i == print(name, ' you will be 100 years old in the year ', str(hundredth_birthday))
    

if __name__ == '__main__':
    run()