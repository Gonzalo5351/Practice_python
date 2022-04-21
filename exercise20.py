# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:
    # Use binary search.

# When you are writing the solution, first try to write it without binary search. Then when you want to try implementing binary search, write a separate function. In the solution I will give an example for how to write a binary search in Python.

def run():
    list_x = []
    another_number = 20

    def list_generator(init_range, end_range, choose_list):
        r = range(init_range, end_range+1)
        ([choose_list.append(i) for i in r])

    def detecting_number(choose_list):
        for i in choose_list:
            if another_number == i:
                return True
        return False

    list_generator(1, 20, list_x)
    print(list_x)
    print(detecting_number(list_x))
    
if __name__ == '__main__':
    run()