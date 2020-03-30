from random import randint
from module import Game, Player

def give_input(question, low_limit = None, high_limit = None):
    """
        since user input is unpredictable hence this function is implemented for taking in appropriate input
    """
    while True:
        try:
            num = int(input(question))

            if low_limit is not None and high_limit is not None and (num < low_limit or num > high_limit):
                raise ValueError('')

            return num

        except ValueError:
            print("That number does not fall in the given range")
        
        except NameError:
            print("That's not a valid input")
    pass



def Play_Game(Sticks_Game, Players):
    """
        This the function where game starts

    Parameters
    ----------
    Sticks_Game : Object of Game class
        DESCRIPTION.
    Players : This is a dictionary where its key is the player and value is the number of sticks 
            he takes.
        DESCRIPTION.

    Returns
    -------
    None.

    """
    turn = randint(1,2)

    while not Sticks_Game.is_over():
        move = None
        if "{}".format(Players[turn]).count("User"):
            move = give_input("{}, enter number of sticks you want to pick, from 1 to 3\n".format(Players[turn]), 1, 3)
        else:
            move = Players[turn].best_move(Sticks_Game.get_sticks())

        print("{} chose {} sticks to reduce.".format(Players[turn], move))
        Sticks_Game.decrease_sticks(move)
        if Sticks_Game.get_sticks() < 1:
            break

        turn = 1 if turn == 2 else 2
    
    print("{} looses the game!".format(Players[turn]))
    pass



if __name__ == "__main__":
    # setting up the game particularly number of sticks required
    total_sticks = give_input("How many sticks do you want to have in the game?(Player choose at least 1 and at most 3)\n")
    Sticks_Game = Game(total_sticks)
    
    # setting up the type of game user wants
    type_of_game = give_input("What type of game setting do you want?\n1: AI vs AI\n2: AI vs User\n3: User vs User\n\nEnter the corresponding number.\n", 1, 3)
    Players = {}
    if type_of_game == 1:
        Players = {
            1: Player(1),
            2: Player(2)
        }
    elif type_of_game == 2:
        Players = {
            1: Player(1),
            2: "User 1"
        }
    else:
        Players = {
            1: "User 1",
            2: "User 2"
        }
    # starting the game
    Play_Game(Sticks_Game, Players)
    pass
