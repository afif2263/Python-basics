def parent_function(person, coins):
    def play_game():
        nonlocal coins
        coins -= 1

        if coins >= 1:
            print("\n " + person + " has " + str(coins) + " coins left.")

        else:
            print("\n " + person + " is out of coins.")
                  
    return play_game

tommy = parent_function("Tommy", 3)
jenny = parent_function ("Jenny", 5)

tommy()
tommy()

jenny()
jenny()
