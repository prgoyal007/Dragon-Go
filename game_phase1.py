# Contains the first 3 introductory phases of the game
# Includes: dragon choice, dragon name, first action
# The tree starts here with all the choices

import classes
import user_input_limits as limits
import misc_variables as misc


# User selects dragon choice
def dragon_pick():
    classes.DragonPick.dragon_choice()


# User selects dragon name
# User is given more game description, and is asked to continue
def game_text_and_dragon_name():
    dragon_name_input = input("What would you like to name your dragon?\n")
    Dragon_Name = classes.DragonName(dragon_name=dragon_name_input)

    print("\nNice choice! " + Dragon_Name.dragon_name + " is an excellent dragon name!\n")

    # Second game description
    print(misc.game_text2)

    empty = ""
    while empty is not limits.yes_no:
        empty = input("\nWould you like to explore late land of Vrubel? (yes/no)\n")
        if empty == "yes":
            player_move()
        elif empty == "no":
            print("""
            Wow, after all this you don't want to explore the land?
            You are clearly not ready for this adventure. Goodbye.
            """)
            quit()
        else:
            print(limits.choice_restriction2)


# User makes first move
# Game starts now
def player_move():
    classes.PlayerMoveChoices1.moves_duplicate_checker()
    classes.PlayerMoveChoices1.player_move_options()
