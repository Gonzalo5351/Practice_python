# 1) Take a list, say for example this one:
#       a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   and write a program that prints out all the elements of the list that are less than 5.

#Extras:

# 2) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 3) Write this in one line of Python.
# 4) Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

def run():
    usr_num = int(input('Please, enter a number between 1 and 89: '))
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    n_list = [i for i in a if i < usr_num]
    print(n_list)

if __name__ == '__main__':
    run()