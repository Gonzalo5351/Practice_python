# 1)Take two lists, say for example these two:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#Extras:

# 2)Randomly generate two lists to test this
# 3)Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

def run():
    counter_1 = 0
    counter_2 = 0
    l_list = []
    m_list = []
    finall_list = []

    #Function to generate two lists of different sizes with random integers. 
    def list_generator(choose_counter, count_level, append_list):
        while choose_counter < count_level:
            generator = random.randint(1, 101)
            append_list.append(generator)
            choose_counter += 1
        

    #Invoked of the function.
    list_generator(counter_1, 20, l_list)
    list_generator(counter_2, 30, m_list)

    #Cycle that compares both lists generated previously and that filters the integers in common in both lists. To then add to these integers in a final list.
    ([finall_list.append(i) for i in m_list if i == i in l_list])

    #Print l_list and m_list to check their content relative to finall_list.
    print(l_list)
    print(m_list)
    #Print final list with common integers in l_list and m_list.
    print(finall_list)

if __name__ == '__main__':
    run()