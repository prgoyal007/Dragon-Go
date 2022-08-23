# Contains all major and functions used for the game
# Includes: Name (player + dragon), Dragon Choice (fire, water etc)

import action_moves as am
import choice_prompts as cp
import game_input_limits as limits
import misc_variables as misc
import game_phase1 as phase_1
import player_variables as pv
import opponent_variables as ov
import numpy as np
import random

# class includes player name and dragon name
# class has been shown how to receive user input when it comes to class PlayerName:
class PlayerName:
    def __init__(self, player_name):
        self.player_name = player_name

    def get_name(self):
        print(self.player_name)


class DragonName:
    def __init__(self, dragon_name):
        self.dragon_name = dragon_name

    def get_dragon_name(self):
        print(self.dragon_name)


"""
name_input = input("What is your name?\n")
Player_Name = PlayerName(player_name=name_input)

dragon_input = input("What would you like to name your dragon?\n")
Dragon_Name = DragonName(dragon_name=dragon_input)

print("\nWelcome " + Player_Name.player_name + ", to Dragon town.")
print("\nNice pick! " + Dragon_Name.dragon_name + " is a great dragon name.")
"""


class DragonUpgrades:
    """
    Overview:
        - Function handles all aspects of HP and attacks related to 'level ups'
        - When user's dragon levels up, HP is reset, new attacks may be added

    Usage:
        - Used and checked frequently
        - Paired with ChoicePrompts; whenever dragon consumes berries/elixir and gains HP and/or levels up
        - Also used after beating trainers and wild dragons, user dragon levels up
        - More description given above the 3 different functions below
    """

    # Used whenever dragon gains 'full health'
    # Dragon HP is reset at level limit
    @staticmethod
    def dragon_health():
        if pv.player_dragon_stats["Level:"] == 1:
            pv.player_dragon_stats["HP:"] = 10
        if pv.player_dragon_stats["Level:"] == 2:
            pv.player_dragon_stats["HP:"] = 15
        if pv.player_dragon_stats["Level:"] == 3:
            pv.player_dragon_stats["HP:"] = 20
        if pv.player_dragon_stats["Level:"] == 4:
            pv.player_dragon_stats["HP:"] = 25
        if pv.player_dragon_stats["Level:"] == 5:
            pv.player_dragon_stats["HP:"] = 30

    # Used whenever dragon 'levels up'
    # Based on level, dragon gains more HP and/or unlocks new attacks
    @staticmethod
    def dragon_level_up():
        pv.player_dragon_stats["Level:"] = pv.player_dragon_stats["Level:"] + 1

        if pv.player_dragon_stats["Dragon Element:"] == "Fire":

            if pv.player_dragon_stats["Level:"] == 2:
                pv.player_dragon_stats["HP:"] = 15
                pv.player_dragon_stats["Attack 2:"] = "Flaming Arrows"
                pv.player_dragon_attacks["Flaming Arrows:"] = 6

            if pv.player_dragon_stats["Level:"] == 3:
                pv.player_dragon_stats["HP:"] = 20

            if pv.player_dragon_stats["Level:"] == 4:
                pv.player_dragon_stats["HP:"] = 25
                pv.player_dragon_stats["Special Attack:"] = "Nuclear Shower"
                pv.player_dragon_attacks["Nuclear Shower:"] = 11

            if pv.player_dragon_stats["Level:"] == 5:
                pv.player_dragon_stats["HP:"] = 30

        if pv.player_dragon_stats["Dragon Element:"] == "Water":

            if pv.player_dragon_stats["Level:"] == 2:
                pv.player_dragon_stats["HP:"] = 15
                pv.player_dragon_stats["Attack 2:"] = "Water Torpedo"
                pv.player_dragon_attacks["Water Torpedo:"] = 5

            if pv.player_dragon_stats["Level:"] == 3:
                pv.player_dragon_stats["HP:"] = 20

            if pv.player_dragon_stats["Level:"] == 4:
                pv.player_dragon_stats["HP:"] = 25
                pv.player_dragon_stats["Special Attack:"] = "Giant Tsunami"
                pv.player_dragon_attacks["Giant Tsunami:"] = 12

            if pv.player_dragon_stats["Level:"] == 5:
                pv.player_dragon_stats["HP:"] = 30

        if pv.player_dragon_stats["Dragon Element:"] == "Earth":

            if pv.player_dragon_stats["Level:"] == 2:
                pv.player_dragon_stats["HP:"] = 15
                pv.player_dragon_stats["Attack 2:"] = "Sand Storm"
                pv.player_dragon_attacks["Sand Storm:"] = 5

            if pv.player_dragon_stats["Level:"] == 3:
                pv.player_dragon_stats["HP:"] = 20

            if pv.player_dragon_stats["Level:"] == 4:
                pv.player_dragon_stats["HP:"] = 25
                pv.player_dragon_stats["Special Attack:"] = "Tectonic Earthquake"
                pv.player_dragon_attacks["Tectonic Earthquake:"] = 12

            if pv.player_dragon_stats["Level:"] == 5:
                pv.player_dragon_stats["HP:"] = 30

        if pv.player_dragon_stats["Dragon Element:"] == "Air":

            if pv.player_dragon_stats["Level:"] == 2:
                pv.player_dragon_stats["HP:"] = 15
                pv.player_dragon_stats["Attack 2:"] = "Tornado"
                pv.player_dragon_attacks["Tornado:"] = 6

            if pv.player_dragon_stats["Level:"] == 3:
                pv.player_dragon_stats["HP:"] = 20

            if pv.player_dragon_stats["Level:"] == 4:
                pv.player_dragon_stats["HP:"] = 25
                pv.player_dragon_stats["Special Attack:"] = "Hurricane"
                pv.player_dragon_attacks["Hurricane:"] = 13

            if pv.player_dragon_stats["Level:"] == 5:
                pv.player_dragon_stats["HP:"] = 30

    # Used whenever dragon gains or loses HP
    # So dragon doesn't go over level limit
    @staticmethod
    def dragon_check_health():
        if pv.player_dragon_stats["HP:"] <= 0:
            print(cp.filler_dialogue[2])
            quit()
        if pv.player_dragon_stats["Level:"] == 1:
            if pv.player_dragon_stats["HP:"] > 10:
                pv.player_dragon_stats["HP:"] = 10

        if pv.player_dragon_stats["Level:"] == 2:
            if pv.player_dragon_stats["HP:"] > 15:
                pv.player_dragon_stats["HP:"] = 15

        if pv.player_dragon_stats["Level:"] == 3:
            if pv.player_dragon_stats["HP:"] > 20:
                pv.player_dragon_stats["HP:"] = 20

        if pv.player_dragon_stats["Level:"] == 4:
            if pv.player_dragon_stats["HP:"] > 25:
                pv.player_dragon_stats["HP:"] = 25

        if pv.player_dragon_stats["Level:"] == 5:
            if pv.player_dragon_stats["HP:"] > 30:
                pv.player_dragon_stats["HP:"] = 30


class DragonPick:
    """
    Overview:
        - Function prompts user with dragon choice
        - User picks dragon element, user's input saves permanently (dragon choice is a permanent value)
        - Picking dragon generates Level: #, HP: #, and attack 1

    Usage:
        - Dragon choice prompted 1 time only, and is permanent
        - But, dragon stats can be accessed and edited throughout game
    """

    @staticmethod
    def dragon_choice():
        print("\nWhat dragon would you like to have as your companion?")
        print("\nA: Fire")
        print("B: Water")
        print("C: Earth")
        print("D: Air")
        print("\nHit 'V' to view all different dragons and their stats")
        print("\nHit 'H' for Game Settings and Hints")

        dragon_element = input("\n>>> ")
        if dragon_element == "a":
            pv.player_dragon_stats = pv.fire_stats
            pv.player_dragon_attacks = pv.fire_attacks
            print("\nYou've selected a {} dragon, nice pick!".format(pv.player_dragon_stats["Dragon Element:"]))
            print(misc.fire_dragon_stats)
            phase_1.game_text_and_dragon_name()

        elif dragon_element == "b":
            pv.player_dragon_stats = pv.water_stats
            pv.player_dragon_attacks = pv.water_attacks
            print("\nYou've selected a {} dragon, nice pick!".format(pv.player_dragon_stats["Dragon Element:"]))
            print(misc.water_dragon_stats)
            phase_1.game_text_and_dragon_name()

        elif dragon_element == "c":
            pv.player_dragon_stats = pv.earth_stats
            pv.player_dragon_attacks = pv.earth_attacks
            print("\nYou've selected a {} dragon, nice pick!".format(pv.player_dragon_stats["Dragon Element:"]))
            print(misc.earth_dragon_stats)
            phase_1.game_text_and_dragon_name()

        elif dragon_element == "d":
            pv.player_dragon_stats = pv.air_stats
            pv.player_dragon_attacks = pv.air_attacks
            print("\nYou've selected a {} dragon, nice pick!".format(pv.player_dragon_stats["Dragon Element:"]))
            print(misc.air_dragon_stats)
            phase_1.game_text_and_dragon_name()

        elif dragon_element == 'v':
            DragonPick.view_dragon_stats()

        elif dragon_element == "h":
            DragonPick.game_settings_and_help()
        else:
            print(limits.choice_restriction1)
            DragonPick.dragon_choice()

    @staticmethod
    def view_dragon_stats():
        print(misc.all_dragon_stats)

        temp = input("\n>>> ")
        if temp == "q":
            DragonPick.dragon_choice()
        else:
            print(limits.choice_restriction4)
            DragonPick.view_dragon_stats()

    @staticmethod
    def game_settings_and_help():
        print(misc.dragon_help)

        temp = input("\n>>> ")
        if temp == 'q':
            DragonPick.dragon_choice()
        else:
            print(limits.choice_restriction4)
            DragonPick.game_settings_and_help()


class DragonDuels:
    @staticmethod
    def trainer_dragon_duels():
        duel_dragon = input("\nWould you like to duel the trainer's dragon? (yes/no)\n")

        if duel_dragon == "yes":
            DragonDuels.trainer_dragon_battle()

        elif duel_dragon == "no":
            escape = np.random.choice(cp.trainer_dragon_escape_choices, p=[0.3, 0.7])

            if escape == cp.trainer_dragon_escape_choices[0]:
                print(cp.trainer_dragon_escape_choices[0])
                PlayerMoveChoices2.player_move_options()

            if escape == cp.trainer_dragon_escape_choices[1]:
                print(cp.trainer_dragon_escape_choices[1])
                DragonDuels.trainer_dragon_battle()

        else:
            print(limits.choice_restriction2)
            DragonDuels.trainer_dragon_duels()

    @staticmethod
    def wild_dragon_duels():
        duel_dragon = input("\nWould you like to duel the wild dragon? (yes/no)\n")

        if duel_dragon == "yes":
            DragonDuels.wild_dragon_battle()

        elif duel_dragon == "no":
            escape = np.random.choice(cp.wild_dragon_escape_choices, p=[0.3, 0.7])

            if escape == cp.wild_dragon_escape_choices[0]:
                print(cp.wild_dragon_escape_choices[0])
                PlayerMoveChoices2.player_move_options()

            if escape == cp.wild_dragon_escape_choices[1]:
                print(cp.wild_dragon_escape_choices[1])
                DragonDuels.wild_dragon_battle()

        else:
            print(limits.choice_restriction2)
            DragonDuels.trainer_dragon_duels()

    @staticmethod
    def trainer_dragon_battle():

    @staticmethod
    def wild_dragon_battle():


# Backward prompt closes game, you exit Vrubel
class PlayerMoveChoices1:
    """
    Overview:
        - Function prompts user with move choices
        - User picks their move, user's input saves permanently (Past actions save in a list and/or file)
        - Game Map is not permanent, User generates map as user moves
        - No duplicates are generated in the 4 prompts


    Usage:
        - Most used function
        - User made typos will print same prompt, not generate new one
    """

    @staticmethod
    def moves_duplicate_checker():
        while True:
            a = ''.join((random.sample(am.forward_left_right_options, 1)))
            b = ''.join((random.sample(am.forward_left_right_options, 1)))
            c = ''.join((random.sample(am.forward_left_right_options, 1)))

            d = (random.sample(am.forward_left_right_options, 1))
            e = (random.sample(am.forward_left_right_options, 1))

            temp_list = [a, b, c]
            my_set = set(temp_list)

            if len(my_set) == len(temp_list):
                PlayerMoveChoices1.moves_duplicate_checker.new_list = list(my_set)
                return PlayerMoveChoices1.moves_duplicate_checker.new_list

            elif len(my_set) < len(temp_list):
                my_set.update(d)

                if len(my_set) == 3:
                    PlayerMoveChoices1.moves_duplicate_checker.new_list = list(my_set)
                    return PlayerMoveChoices1.moves_duplicate_checker.new_list

                if len(my_set) < 3:
                    my_set.update(e)
                    PlayerMoveChoices1.moves_duplicate_checker.new_list = list(my_set)
                    return PlayerMoveChoices1.moves_duplicate_checker.new_list

            else:
                PlayerMoveChoices1.moves_duplicate_checker()

    @staticmethod
    def player_move_options():
        print("What direction would you like to move?\n")
        print("Forward: ", PlayerMoveChoices1.moves_duplicate_checker.new_list[0])
        print("Backward: ", am.backward_options[0])
        print("Left: ", PlayerMoveChoices1.moves_duplicate_checker.new_list[1])
        print("Right: ", PlayerMoveChoices1.moves_duplicate_checker.new_list[2])
        print("\nHit 'H' for Game Settings and Hints")

        move_choice = input("\n>>> ")
        if move_choice == "forward":
            if PlayerMoveChoices1.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[0]:
                ChoicePrompts.trainer_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[1]:
                ChoicePrompts.game_continuity_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[2]:
                ChoicePrompts.wild_dragon_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[3]:
                ChoicePrompts.wild_berries_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[4]:
                ChoicePrompts.elixir_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[5]:
                ChoicePrompts.dark_cave_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[6]:
                ChoicePrompts.boulder_choices()

        elif move_choice == "backward":
            print("You chose to exit Vrubel. You were clearly not up for this adventure.")
            print("You lose. Goodbye.")
            quit()

        elif move_choice == "left":
            if PlayerMoveChoices1.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[0]:
                ChoicePrompts.trainer_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[1]:
                ChoicePrompts.game_continuity_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[2]:
                ChoicePrompts.wild_dragon_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[3]:
                ChoicePrompts.wild_berries_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[4]:
                ChoicePrompts.elixir_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[5]:
                ChoicePrompts.dark_cave_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[6]:
                ChoicePrompts.boulder_choices()

        elif move_choice == "right":
            if PlayerMoveChoices1.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[0]:
                ChoicePrompts.trainer_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[1]:
                ChoicePrompts.game_continuity_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[2]:
                ChoicePrompts.wild_dragon_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[3]:
                ChoicePrompts.wild_berries_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[4]:
                ChoicePrompts.elixir_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[5]:
                ChoicePrompts.dark_cave_choices()

            if PlayerMoveChoices1.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[6]:
                ChoicePrompts.boulder_choices()

        elif move_choice == 'h':
            PlayerMoveChoices1.game_settings_and_help()

        else:
            print(limits.choice_restriction3)
            PlayerMoveChoices1.player_move_options()

    @staticmethod
    def game_settings_and_help():
        print(misc.dragon_help)

        temp = input("\n>>> ")
        if temp == 'q':
            PlayerMoveChoices1.player_move_options()
        else:
            print(limits.choice_restriction4)
            PlayerMoveChoices1.game_settings_and_help()


# Backward prompt takes you a step back
class PlayerMoveChoices2:
    """
    Overview:
        - Function prompts user with move choices
        - User picks their move, user's input saves permanently (Past actions save in a list and/or file)
        - Game Map is not permanent, User generates map as user moves
        - No duplicates are generated in the 4 prompts


    Usage:
        - Most used function
        - User made typos will print same prompt, not generate new one
    """

    @staticmethod
    def moves_duplicate_checker():
        while True:
            a = ''.join((random.sample(am.forward_left_right_options, 1)))
            b = ''.join((random.sample(am.forward_left_right_options, 1)))
            c = ''.join((random.sample(am.forward_left_right_options, 1)))

            d = (random.sample(am.forward_left_right_options, 1))
            e = (random.sample(am.forward_left_right_options, 1))

            temp_list = [a, b, c]
            my_set = set(temp_list)

            if len(my_set) == len(temp_list):
                PlayerMoveChoices2.moves_duplicate_checker.new_list = list(my_set)
                return PlayerMoveChoices2.moves_duplicate_checker.new_list

            elif len(my_set) < len(temp_list):
                my_set.update(d)

                if len(my_set) == 3:
                    PlayerMoveChoices2.moves_duplicate_checker.new_list = list(my_set)
                    return PlayerMoveChoices2.moves_duplicate_checker.new_list

                if len(my_set) < 3:
                    my_set.update(e)
                    PlayerMoveChoices2.moves_duplicate_checker.new_list = list(my_set)
                    return PlayerMoveChoices2.moves_duplicate_checker.new_list

            else:
                PlayerMoveChoices2.moves_duplicate_checker()

    @staticmethod
    def player_move_options():
        print("What direction would you like to move?\n")
        print("Forward: ", PlayerMoveChoices2.moves_duplicate_checker.new_list[0])
        print("Backward: ", am.backward_options[1])
        print("Left: ", PlayerMoveChoices2.moves_duplicate_checker.new_list[1])
        print("Right: ", PlayerMoveChoices2.moves_duplicate_checker.new_list[2])
        print("\nHit 'H' for Game Settings and Hints")

        move_choice = input("\n>>> ")
        if move_choice == "forward":
            if PlayerMoveChoices2.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[0]:
                ChoicePrompts.trainer_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[1]:
                ChoicePrompts.game_continuity_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[2]:
                ChoicePrompts.wild_dragon_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[3]:
                ChoicePrompts.wild_berries_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[4]:
                ChoicePrompts.elixir_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[5]:
                ChoicePrompts.dark_cave_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[0] == am.forward_left_right_options[6]:
                ChoicePrompts.boulder_choices()

        elif move_choice == "backward":
            print(am.backward_options[1])
            PlayerMoveChoices1.player_move_options()

        elif move_choice == "left":
            if PlayerMoveChoices2.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[0]:
                ChoicePrompts.trainer_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[1]:
                ChoicePrompts.game_continuity_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[2]:
                ChoicePrompts.wild_dragon_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[3]:
                ChoicePrompts.wild_berries_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[4]:
                ChoicePrompts.elixir_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[5]:
                ChoicePrompts.dark_cave_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[1] == am.forward_left_right_options[6]:
                ChoicePrompts.boulder_choices()

        elif move_choice == "right":
            if PlayerMoveChoices2.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[0]:
                ChoicePrompts.trainer_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[1]:
                ChoicePrompts.game_continuity_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[2]:
                ChoicePrompts.wild_dragon_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[3]:
                ChoicePrompts.wild_berries_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[4]:
                ChoicePrompts.elixir_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[5]:
                ChoicePrompts.dark_cave_choices()

            if PlayerMoveChoices2.moves_duplicate_checker.new_list[2] == am.forward_left_right_options[6]:
                ChoicePrompts.boulder_choices()

        elif move_choice == 'h':
            PlayerMoveChoices2.game_settings_and_help()

        else:
            print(limits.choice_restriction3)
            PlayerMoveChoices2.player_move_options()

    @staticmethod
    def game_settings_and_help():
        print(misc.dragon_help)

        temp = input("\n>>> ")
        if temp == 'q':
            PlayerMoveChoices2.player_move_options()
        else:
            print(limits.choice_restriction4)
            PlayerMoveChoices2.game_settings_and_help()


class ChoicePrompts:
    """
    Overview:
        - Class contains all choice prompts
        - User picks their move, and move leads them here
        - All choice prompts are assigned their own functions
        - Each function has its own prompt list that generates when function prompt is activated


    Usage:
        - Most used function, tied with PlayerMoveChoices
        - Duels/Battles are looped to different Class
        - Rest is looped inside here or back to PlayerMoveChoices

        - Stat based prompts like consuming berries and elixir
            - Lead to DragonUpgrade Class that updates and tracks any dragon stat changes (behind the scenes)
            - Whenever changes are made, User is prompted option to view dragon stats
    """

    @staticmethod
    def trainer_choices():
        print(am.forward_left_right_continuity[0])

        trainer_choices = np.random.choice(cp.trainer_choices, p=[0.7, 0.25, 0.05])

        if trainer_choices == cp.trainer_choices[0]:
            print(cp.trainer_choices[0])
            ChoicePrompts.trainer_dragon_choices()

        if trainer_choices == cp.trainer_choices[1]:
            print(cp.trainer_choices[1])
            print(cp.filler_dialogue[0])
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

        if trainer_choices == cp.trainer_choices[2]:
            print(cp.trainer_choices[2])
            print(cp.filler_dialogue[0])
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

    @staticmethod
    def trainer_dragon_choices():
        trainer_dragon = np.random.choice(cp.trainer_dragon_choices, p=[0.125, 0.049, 0.225, 0.1, 0.001, 0.125, 0.049,
                                                                        0.225, 0.1, 0.001])

        if trainer_dragon == cp.trainer_dragon_choices[0]:
            print(cp.trainer_dragon_choices[0])
            ov.opponent_dragon_stats = ov.fire_stats_2
            ov.opponent_dragon_attacks = ov.fire_attacks_2
            DragonDuels.trainer_dragon_duels()

        if trainer_dragon == cp.trainer_dragon_choices[1]:
            print(cp.trainer_dragon_choices[1])
            ov.opponent_dragon_stats = ov.fire_stats_4
            ov.opponent_dragon_attacks = ov.fire_attacks_4
            DragonDuels.trainer_dragon_duels()

        if trainer_dragon == cp.trainer_dragon_choices[2]:
            print(cp.trainer_dragon_choices[2])
            ov.opponent_dragon_stats = ov.water_stats_1
            ov.opponent_dragon_attacks = ov.water_attacks_1
            DragonDuels.trainer_dragon_duels()

        if trainer_dragon == cp.trainer_dragon_choices[3]:
            print(cp.trainer_dragon_choices[3])
            ov.opponent_dragon_stats = ov.water_stats_3
            ov.opponent_dragon_attacks = ov.water_attacks_3
            DragonDuels.trainer_dragon_duels()

        if trainer_dragon == cp.trainer_dragon_choices[4]:
            print(cp.trainer_dragon_choices[4])
            ov.opponent_dragon_stats = ov.water_stats_5
            ov.opponent_dragon_attacks = ov.water_attacks_5
            DragonDuels.trainer_dragon_duels()

        if trainer_dragon == cp.trainer_dragon_choices[5]:
            print(cp.trainer_dragon_choices[5])
            ov.opponent_dragon_stats = ov.earth_stats_2
            ov.opponent_dragon_attacks = ov.earth_attacks_2
            DragonDuels.trainer_dragon_duels()

        if trainer_dragon == cp.trainer_dragon_choices[6]:
            print(cp.trainer_dragon_choices[6])
            ov.opponent_dragon_stats = ov.earth_stats_4
            ov.opponent_dragon_attacks = ov.earth_attacks_4
            DragonDuels.trainer_dragon_duels()

        if trainer_dragon == cp.trainer_dragon_choices[7]:
            print(cp.trainer_dragon_choices[7])
            ov.opponent_dragon_stats = ov.air_stats_1
            ov.opponent_dragon_attacks = ov.air_attacks_1
            DragonDuels.trainer_dragon_duels()

        if trainer_dragon == cp.trainer_dragon_choices[8]:
            print(cp.trainer_dragon_choices[8])
            ov.opponent_dragon_stats = ov.air_stats_3
            ov.opponent_dragon_attacks = ov.air_attacks_3
            DragonDuels.trainer_dragon_duels()

        if trainer_dragon == cp.trainer_dragon_choices[9]:
            print(cp.trainer_dragon_choices[9])
            ov.opponent_dragon_stats = ov.air_stats_5
            ov.opponent_dragon_attacks = ov.air_attacks_5
            DragonDuels.trainer_dragon_duels()

    @staticmethod
    def game_continuity_choices():
        print(am.forward_left_right_continuity[1])

        game_continuation = np.random.choice(cp.game_continuity_choices, p=[0.14, 0.18, 0.18, 0.18, 0.18, 0.14])

        if game_continuation == cp.game_continuity_choices[0]:
            print(cp.game_continuity_choices[0])
            ChoicePrompts.wild_berries_choices()

        if game_continuation == cp.game_continuity_choices[1]:
            print(cp.game_continuity_choices[1])
            ChoicePrompts.boulder_choices()

        if game_continuation == cp.game_continuity_choices[2]:
            print(cp.game_continuity_choices[2])
            ChoicePrompts.trainer_choices()

        if game_continuation == cp.game_continuity_choices[3]:
            print(cp.game_continuity_choices[3])
            ChoicePrompts.wild_dragon_choices()

        if game_continuation == cp.game_continuity_choices[4]:
            print(cp.game_continuity_choices[4])
            ChoicePrompts.dark_cave_choices()

        if game_continuation == cp.game_continuity_choices[5]:
            print(cp.game_continuity_choices[5])
            ChoicePrompts.elixir_choices()

    @staticmethod
    def wild_dragon_choices():
        wild_dragon = np.random.choice(cp.wild_dragon_choices, p=[0.125, 0.049, 0.225, 0.06, 0.001, 0.125, 0.049, 0.225,
                                                                  0.06, 0.001, 0.08])

        if wild_dragon == cp.wild_dragon_choices[0]:
            print(cp.wild_dragon_choices[0])
            ov.opponent_dragon_stats = ov.fire_stats_1
            ov.opponent_dragon_attacks = ov.fire_attacks_1
            DragonDuels.wild_dragon_duels()

        if wild_dragon == cp.wild_dragon_choices[1]:
            print(cp.wild_dragon_choices[1])
            ov.opponent_dragon_stats = ov.fire_stats_3
            ov.opponent_dragon_attacks = ov.fire_attacks_3
            DragonDuels.wild_dragon_duels()

        if wild_dragon == cp.wild_dragon_choices[2]:
            print(cp.wild_dragon_choices[2])
            ov.opponent_dragon_stats = ov.fire_stats_5
            ov.opponent_dragon_attacks = ov.fire_attacks_5
            DragonDuels.wild_dragon_duels()

        if wild_dragon == cp.wild_dragon_choices[3]:
            print(cp.wild_dragon_choices[3])
            ov.opponent_dragon_stats = ov.water_stats_2
            ov.opponent_dragon_attacks = ov.water_attacks_2
            DragonDuels.wild_dragon_duels()

        if wild_dragon == cp.wild_dragon_choices[4]:
            print(cp.wild_dragon_choices[4])
            ov.opponent_dragon_stats = ov.water_stats_4
            ov.opponent_dragon_attacks = ov.water_attacks_4
            DragonDuels.wild_dragon_duels()

        if wild_dragon == cp.wild_dragon_choices[5]:
            print(cp.wild_dragon_choices[5])
            ov.opponent_dragon_stats = ov.earth_stats_1
            ov.opponent_dragon_attacks = ov.earth_attacks_1
            DragonDuels.wild_dragon_duels()

        if wild_dragon == cp.wild_dragon_choices[6]:
            print(cp.wild_dragon_choices[6])
            ov.opponent_dragon_stats = ov.earth_stats_3
            ov.opponent_dragon_attacks = ov.earth_attacks_3
            DragonDuels.wild_dragon_duels()

        if wild_dragon == cp.wild_dragon_choices[7]:
            print(cp.wild_dragon_choices[7])
            ov.opponent_dragon_stats = ov.earth_stats_5
            ov.opponent_dragon_attacks = ov.earth_attacks_5
            DragonDuels.wild_dragon_duels()

        if wild_dragon == cp.wild_dragon_choices[8]:
            print(cp.wild_dragon_choices[8])
            ov.opponent_dragon_stats = ov.air_stats_2
            ov.opponent_dragon_attacks = ov.air_attacks_2
            DragonDuels.wild_dragon_duels()

        if wild_dragon == cp.wild_dragon_choices[9]:
            print(cp.wild_dragon_choices[9])
            ov.opponent_dragon_stats = ov.air_stats_4
            ov.opponent_dragon_attacks = ov.air_attacks_4
            DragonDuels.wild_dragon_duels()

        if wild_dragon == cp.wild_dragon_choices[10]:
            print(cp.wild_dragon_choices[10])
            print(cp.filler_dialogue[1])
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

    @staticmethod
    def wild_berries_choices():
        wild_berries = np.random.choice(cp.wild_berry_choices, p=[0.075, 0.05, 0.025, 0.4, 0.25, 0.1, 0.1])

        eat_wild_berries = input("\nWould you like to feed your dragon the wild berries? (yes/no)\n")

        if eat_wild_berries == "yes":
            if wild_berries == cp.wild_berry_choices[0]:
                print(cp.wild_berry_choices[0])
                print(cp.filler_dialogue[2])
                quit()

            if wild_berries == cp.wild_berry_choices[1]:
                print(cp.wild_berry_choices[1])
                DragonUpgrades.dragon_health()
                ChoicePrompts.view_stats_berries()

            if wild_berries == cp.wild_berry_choices[2]:
                print(cp.wild_berry_choices[2])
                DragonUpgrades.dragon_level_up()
                ChoicePrompts.view_stats_berries()

            if wild_berries == cp.wild_berry_choices[3]:
                print(cp.wild_berry_choices[3])
                pv.player_dragon_stats["HP:"] = pv.player_dragon_stats["HP:"] + 1
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_berries()

            if wild_berries == cp.wild_berry_choices[4]:
                print(cp.wild_berry_choices[4])
                pv.player_dragon_stats["HP:"] = pv.player_dragon_stats["HP:"] + 3
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_berries()

            if wild_berries == cp.wild_berry_choices[5]:
                print(cp.wild_berry_choices[5])
                pv.player_dragon_stats["HP:"] = pv.player_dragon_stats["HP:"] + 5
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_berries()

            if wild_berries == cp.wild_berry_choices[6]:
                print(cp.wild_berry_choices[6])
                pv.player_dragon_stats["HP:"] = pv.player_dragon_stats["HP:"] - 5
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_berries()

        elif eat_wild_berries == "no":
            print(cp.filler_dialogue[3])
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

        else:
            print(limits.choice_restriction2)
            ChoicePrompts.wild_berries_choices()

    @staticmethod
    def elixir_choices():
        elixir = np.random.choice(cp.elixir_choices, p=[0.075, 0.05, 0.025, 0.4, 0.25, 0.1, 0.1])

        drink_elixir = input("\nWould you like to give your dragon the bottle of elixir? (yes/no)\n")

        if drink_elixir == "yes":
            if elixir == cp.elixir_choices[0]:
                print(cp.elixir_choices[0])
                print(cp.filler_dialogue[2])
                quit()

            if elixir == cp.elixir_choices[1]:
                print(cp.elixir_choices[1])
                DragonUpgrades.dragon_health()
                ChoicePrompts.view_stats_elixir()

            if elixir == cp.elixir_choices[2]:
                print(cp.elixir_choices[2])
                DragonUpgrades.dragon_level_up()
                ChoicePrompts.view_stats_elixir()

            if elixir == cp.elixir_choices[3]:
                print(cp.elixir_choices[3])
                pv.player_dragon_stats["HP:"] = pv.player_dragon_stats["HP:"] + 1
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_elixir()

            if elixir == cp.elixir_choices[4]:
                print(cp.elixir_choices[4])
                pv.player_dragon_stats["HP:"] = pv.player_dragon_stats["HP:"] + 3
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_elixir()

            if elixir == cp.elixir_choices[5]:
                print(cp.elixir_choices[5])
                pv.player_dragon_stats["HP:"] = pv.player_dragon_stats["HP:"] + 5
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_elixir()

            if elixir == cp.elixir_choices[6]:
                print(cp.elixir_choices[6])
                pv.player_dragon_stats["HP:"] = pv.player_dragon_stats["HP:"] - 5
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_elixir()

        elif drink_elixir == "no":
            print(cp.filler_dialogue[3])
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

        else:
            print(limits.choice_restriction2)
            ChoicePrompts.elixir_choices()

    @staticmethod
    def dark_cave_choices():
        dark_cave = np.random.choice(cp.dark_cave_choices, p=[0.2, 0.2, 0.2, 0.2, 0.2])

        enter_dark_cave = input("\nWould you like to enter the dark cave? (yes/no)\n")

        if enter_dark_cave == "yes":
            if dark_cave == cp.dark_cave_choices[0]:
                print(cp.dark_cave_choices[0])
                ChoicePrompts.wild_dragon_choices()

            if dark_cave == cp.dark_cave_choices[1]:
                print(cp.dark_cave_choices[1])
                ChoicePrompts.wild_berries_choices()

            if dark_cave == cp.dark_cave_choices[2]:
                print(cp.dark_cave_choices[2])
                ChoicePrompts.elixir_choices()

            if dark_cave == cp.dark_cave_choices[3]:
                print(cp.dark_cave_choices[3])
                print("You lose. Goodbye.")
                quit()

            if dark_cave == cp.dark_cave_choices[4]:
                print(cp.dark_cave_choices[4])

                exit_dark_cave = input("Would you like to exit the cave? (yes/no)\n")

                if exit_dark_cave == "yes":
                    print("You've safely exited out of the cave.")
                    PlayerMoveChoices2.moves_duplicate_checker()
                    PlayerMoveChoices2.player_move_options()
                elif exit_dark_cave == "no":
                    print("\nFor stalling inside the cave, a set of spiked rocks split you and your dragon in half.")
                    print("You both die. You lose. Goodbye.")
                    quit()
                else:
                    print(exit_dark_cave)

        elif enter_dark_cave == "no":
            print(cp.filler_dialogue[3])
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

        else:
            print(limits.choice_restriction2)
            ChoicePrompts.dark_cave_choices()

    @staticmethod
    def boulder_choices():
        boulder = np.random.choice(cp.boulder_choices, p=[0.5, 0.2, 0.2, 0.1])

        dodge_boulder = input("\nWould you like to dodge the incoming boulder? (yes/no)\n")

        if dodge_boulder == "yes":
            if boulder == cp.boulder_choices[0]:
                print(cp.boulder_choices[0])
                print(cp.filler_dialogue[4])
                PlayerMoveChoices2.moves_duplicate_checker()
                PlayerMoveChoices2.player_move_options()

            if boulder == cp.boulder_choices[1]:
                print(cp.boulder_choices[1])
                print(cp.filler_dialogue[2])
                quit()

            if boulder == cp.boulder_choices[2]:
                print(cp.boulder_choices[2])
                print(cp.filler_dialogue[5])
                quit()

            if boulder == cp.boulder_choices[3]:
                print(cp.boulder_choices[3])
                print(cp.filler_dialogue[6])
                quit()

        elif dodge_boulder == "no":
            print("\nThe boulder crushes you and your dragon, which kills you both instantly.")
            print("You lose. Goodbye.")
            quit()

        else:
            print(limits.choice_restriction2)
            ChoicePrompts.boulder_choices()

    @staticmethod
    def view_stats_berries():
        print("\nHit 'X' to view your dragon's stats")
        print("\nHit 'A' to view your dragon's attacks")
        print("\nHit 'S' to skip and continue")

        stats = input("\n>>> ")
        if stats == "x":
            for x, y in pv.player_dragon_stats.items():
                print(x, y)
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

        elif stats == "a":
            for x, y in pv.player_dragon_attacks.items():
                print(x, y)
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

        elif stats == "s":
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

        else:
            print(limits.choice_restriction5)
            ChoicePrompts.view_stats_berries()

    @staticmethod
    def view_stats_elixir():
        print("\nHit 'X' to view your dragon's stats")
        print("\nHit 'A' to view your dragon's attacks")
        print("\nHit 'S' to skip and continue")

        stats = input("\n>>> ")
        if stats == "x":
            for x, y in pv.player_dragon_stats.items():
                print(x, y)
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

        elif stats == "a":
            for x, y in pv.player_dragon_attacks.items():
                print(x, y)
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

        elif stats == "s":
            PlayerMoveChoices2.moves_duplicate_checker()
            PlayerMoveChoices2.player_move_options()

        else:
            print(limits.choice_restriction5)
            ChoicePrompts.view_stats_elixir()
