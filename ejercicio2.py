# April 14, 2022

#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def run():
    num_usr = int(input('Pleas, enter a number: '))


    if num_usr % 2 == 0:
        print('The number enterd is even.')
    else:
        print('The number enterd is odd.')
    
    if num_usr % 4 == 0:
        print('And it is also a multiple of 4')

    num = int(input('Now please enter a new number: '))
    check = int(input('Now enter another number different from the last: '))

    if check % num == 0:
        print(check, ' divides evenly into', num)
    else:
        print(check, ' does not divide evenly on ', num)

if __name__ == '__main__':
    run()