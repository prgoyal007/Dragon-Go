# Contains main game file
# Game will run and start here
# Includes: player name, choice to play game or not

import user_input_limits as limits
import game_phase1 as phase_1
import classes
import misc_variables as misc

# player is asked for their name
name_input = input("What is your name, adventurer?\n")
Player_Name = classes.PlayerName(player_name=name_input)

print("\nWelcome " + Player_Name.player_name + ", to Dragoneapolis, the golden city of dragons!")

# first game description
print(misc.game_text1)

# player is asked if he wants to play
empty = ""

while empty is not limits.yes_no:
    empty = input("Would you like to open the package? (yes/no):\n")
    if empty == "yes":
        print("""
        You open the package to find out that it contains dragons!
        Unfortunately, the package is enchanted which only allows you to select one dragon.
        """)
        phase_1.dragon_pick()

    elif empty == "no":
        print("""
        Oh no! You've decided not to open the package.
        For not accepting Sensei Roku's gift, you've been exiled out of Dragoneapolis.
        As you reach the edge of Dragoneapolis, a legendary level 5 Hybrid Dragon swoops in and kills you.
        """)
        print("Sorry " + Player_Name.player_name + ". You died. Goodbye.\n")
        quit()

    else:
        print(limits.choice_restriction2)
