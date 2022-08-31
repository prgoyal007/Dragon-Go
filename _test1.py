import action_moves as am
import game_input_limits as limits
import misc_variables as misc
import random


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
            print("\nYou chose to exit Vrubel. You were clearly not up for this adventure.")
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
            print(limits.choice_restriction1)
            PlayerMoveChoices1.game_settings_and_help()


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
            print(limits.choice_restriction1)
            PlayerMoveChoices2.game_settings_and_help()


PlayerMoveChoices1.moves_duplicate_checker()
PlayerMoveChoices1.player_move_options()
