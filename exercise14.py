# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import random

def run():
    counter_1 = 0
    counter_2 = 0
    l_list = []
    m_list = []
    

    def list_generator(choose_counter, count_level, append_list):
        while choose_counter < count_level:
            generator = random.randint(1, 101)
            append_list.append(generator)
            choose_counter += 1

    def remove_duplicated(choose_list):
        choose_list = set(choose_list)
        choose_list = list(choose_list)
        return choose_list
    
    list_generator(counter_1, 20, l_list)
    print(l_list)

    print(remove_duplicated(l_list))

if __name__ == '__main__':
    run()