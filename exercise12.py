# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

# Concepts to practice
    # Lists and properties of lists
    # List comprehensions (maybe)
    # Functions


def run():
    a = [5, 10, 15, 20, 25]
    b = []

    def first_last(list_1, list_2):
        list_2.append(list_1[::len(list_1)-1])
        print(list_2)
    
    first_last(a, b,)
    

if __name__ == '__main__':
    run()