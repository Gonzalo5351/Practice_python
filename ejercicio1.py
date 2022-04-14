# Crea un programa que le pida al usuario que ingrese su nombre y su edad.
# Imprime un menasje dirigido a ellos que les indique el año en que cumplirán 100 años 
# 
# Extras:
# 1: Agregue al programa anterior pidiéndole al usuario otro número e imprimiendo tantas
# copias del mensaje anterior. (Pista: El orden de las operaciones existe en Python).
# 2: Imprima esa cantidad de copias del mensaje anterior en lineas separadas. (Pista: 
# la cadena "\n" es lo mismo que precionar ENTER)

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