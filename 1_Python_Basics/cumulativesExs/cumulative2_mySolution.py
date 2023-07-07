# Rock , Paper, Scissors
# At this point we are supose to use only basic control statements
# if while for 

import random
                         
wins = 0
losses = 0
ties = 0

machine_move = ''
player_choice = ''
player_move = ''

while player_choice != 'r' or player_choice != 's' or player_choice != 'p' or player_choice != 'q':

    machine_move_gen = random.randint(0,2)
    if machine_move_gen == 0:
        machine_move = 'rock'
    elif machine_move_gen == 1:
        machine_move = 'scissors'
    elif machine_move_gen == 2:
        machine_move = 'paper'

    print("\nWins : " + str(wins) + "\nLosses : " +str(losses) + "\nTies:" + str(ties))
    print("\nEnter your move (r)ock (p)aper (s)cissors or (q)uit.\n")
    player_choice = input()
    
    if player_choice == 'r':
        print("You have choosen (r)ock.")
        player_move = 'rock'
        
        if machine_move == 'rock':
            print("There is a tie, Machine has " + machine_move)
            ties += 1
        
        elif machine_move == 'scissors':
            print("You Win, Machine has " + machine_move)
            wins += 1

        elif machine_move == 'paper':
            print("You lose, Machine has " + machine_move)
            losses += 1
        continue


    elif player_choice == 'p':
        print("You have choosen (p)aper ")
        player_move = 'paper'
        
        if machine_move == 'rock':
            print("You Win, Machine has " + machine_move)
            wins += 1
        
        elif machine_move == 'scissors':
            print("You lose, Machine has " + machine_move)
            losses += 1

        elif machine_move == 'paper':
            print("There is a tie, Machine has " + machine_move)
            ties += 1
        continue

    elif player_choice == 's':
        print("You have choosen (s)cissors ")
        player_move = 'scissors'
        
        if machine_move == 'rock':
            print("You lose, Machine has " + machine_move)
            losses += 1
        
        elif machine_move == 'scissors':
            print("There is a tie, Machine has " + machine_move)
            ties += 1

        elif machine_move == 'paper':
            print("You Win, Machine has " + machine_move)
            wins += 1
        continue
    
    elif player_choice == 'q':
        print("Good bye!")
        print("\nWins : " + str(wins) + "\nLosses : " + str(losses) + "\nTies:" +str(ties))
        break

    else:
        print("Invalid Option. \n Try Again")
        continue
