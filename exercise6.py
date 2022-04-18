#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def run():
    phrase = input('Please, enter a phrase: ')
    phras = phrase.replace(' ', '')
    phra = phras.lower()
    
    def palindrome():
        if phra == phra[::-1]:
            return True
        else:
            return False
    
    if palindrome() == True:
        print('The phrase is a plaindrome.')
    else:
        print('The prhase is not palindrome.')

if __name__ == '__main__':
    run()