import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        class RPS(Enum):
            Rock = 1
            Paper = 2
            Scissors = 3
        playerchoice = input ("Enter...\n 1 For Rock \n 2 fo Paper\n 3 for Scissor: \n \n  ")

        player = int(playerchoice)

        if playerchoice not in ["1", "2", "3"]:
            print("\n You must enter 1, 2, 3.")
            return play_rps()
        

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("")
        print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
        print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
        print("")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                print("You Win!!")

            elif player == 2 and computer == 1:
                player_wins += 1
                print("You win!!")
            elif player == 3 and computer == 2:
                player_wins += 1
                print("You win!!")
            elif player == computer:
                player_wins += 1
                print ("Tie game!!")
            else:
                python_wins += 1
                print("Python wins!") 
        
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print ("\n Game count:" + str(game_count))
        print ("\n Player count:" + str(player_wins))
        print ("\n python count:" + str(python_wins))


        print("\n play agian?")
        while True:
            playagain = input("\nY for Yes or \n Q for Quit")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\nThank you for playing")
            playagain = False

            sys.exit("Bye!")
    return play_rps

play = rps()
play()




