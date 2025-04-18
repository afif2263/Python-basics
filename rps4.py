import sys
import random
from enum import Enum
game_count = 0
class RPS(Enum):
        Rock = 1
        Paper = 2
        Scissors = 3
def play_rps():
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

            if player == 1 and computer == 3:
                print("You Win!!")
            elif player == 2 and computer == 1:
                print("You win!!")
            elif player == 3 and computer == 2:
                print("You win!!")
            elif player == computer:
                print ("Tie game!!")
            else:
                print("Python wins!") 
        
        game_result = decide_winner(player, computer)
        print(game_result)

        global game_count
        game_count += 1
        print ("\n Game count:" + str(game_count))


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

play_rps()
