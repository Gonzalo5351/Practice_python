# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)


def run():
    print('Wellcome to Rock-Paper-Scissors game.')

    player_1 = 0
    player_2 = 0


    player_1 = (input('Player 1, choose an option: \n 1) For rock \n 2) For paper. \n 3) For Scissors.\n -> '))
    player_2 = (input('Player 2, choose an option: \n 1) For rock \n 2) For paper. \n 3) For Scissors.\n -> '))
    
    if player_1 == 1 and player_2 == 3:
        print('Player 1 choose: rock \nAnd player 2 choose: scissors  \nPlayer 1 win')
    



    # piedra = 1
    # papel = 2
    # tijera = 3

    # a = 'piedra gana'
    # b = 'papale gana'
    # c = 'tijera gana'

    # def jugadas_ganadoras(): 
    #     if piedra + tijera:
    #         print(a, 'win')
    #     elif papel + piedra:
    #         print(b, 'gana')
    #     elif tijera + papel:
    #         print(c, 'gana')

    

if __name__ == '__main__':
    run()