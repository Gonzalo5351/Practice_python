def run():
    list_x = []

    def list_generator(init_range, end_range, choose_list):
        r = range(init_range, end_range +1)
        ([choose_list.append(i) for i in r])


    def detecting_number_binary(value, choose_list):
        beggining = 0
        final = len(choose_list) -1
        while beggining <= final:
            pointer = (beggining + final) //2
            if value == choose_list[pointer]:
                return pointer
            elif value > choose_list[pointer]:
                beggining = pointer +1
            else:
                final = pointer -1
        return None


    def find_value(value, choose_list):
        search_anwer = detecting_number_binary(value, choose_list)
        if search_anwer is None:
            return f'Number {value} not find'
        else:
            return f'Number {value} is in the position {search_anwer}'
    

                
    list_generator(1, 20, list_x)
    print(find_value(15, list_x))

if __name__ == '__main__':
    run()