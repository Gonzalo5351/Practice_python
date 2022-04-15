#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def run():
    usr_num = int(input('Please, enter a number: '))
    ([print(i) for i in range(1, usr_num +1) if usr_num % i == 0]) 
    
    # A list comprehension inside a tuple?. Anyway, it works.  


if __name__ == '__main__':
    run()