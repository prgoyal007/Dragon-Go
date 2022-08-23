import misc_variables as misc
import user_input_limits as limits
import action_moves as am
import numpy as np
import choice_prompts as cp


class ChoicePrompts:
    """
    Needs description
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
            PlayerMoveChoices2.player_move_options()

        if trainer_choices == cp.trainer_choices[2]:
            print(cp.trainer_choices[2])
            print(cp.filler_dialogue[0])
            PlayerMoveChoices2.player_move_options()

    @staticmethod
    def trainer_dragon_choices():
        trainer_dragon = np.random.choice(cp.trainer_dragon_choices, p=[0.125, 0.049, 0.225, 0.1, 0.001, 0.125, 0.049,
                                                                        0.225, 0.1, 0.001])

        if trainer_dragon == cp.trainer_dragon_choices[0]:
            print(cp.trainer_dragon_choices[0])

        if trainer_dragon == cp.trainer_dragon_choices[1]:
            print(cp.trainer_dragon_choices[1])

        if trainer_dragon == cp.trainer_dragon_choices[2]:
            print(cp.trainer_dragon_choices[2])

        if trainer_dragon == cp.trainer_dragon_choices[3]:
            print(cp.trainer_dragon_choices[3])

        if trainer_dragon == cp.trainer_dragon_choices[4]:
            print(cp.trainer_dragon_choices[4])

        if trainer_dragon == cp.trainer_dragon_choices[5]:
            print(cp.trainer_dragon_choices[5])

        if trainer_dragon == cp.trainer_dragon_choices[6]:
            print(cp.trainer_dragon_choices[6])

        if trainer_dragon == cp.trainer_dragon_choices[7]:
            print(cp.trainer_dragon_choices[7])

        if trainer_dragon == cp.trainer_dragon_choices[8]:
            print(cp.trainer_dragon_choices[8])

        if trainer_dragon == cp.trainer_dragon_choices[9]:
            print(cp.trainer_dragon_choices[9])

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

        if wild_dragon == cp.wild_dragon_choices[1]:
            print(cp.wild_dragon_choices[1])

        if wild_dragon == cp.wild_dragon_choices[2]:
            print(cp.wild_dragon_choices[2])

        if wild_dragon == cp.wild_dragon_choices[3]:
            print(cp.wild_dragon_choices[3])

        if wild_dragon == cp.wild_dragon_choices[4]:
            print(cp.wild_dragon_choices[4])

        if wild_dragon == cp.wild_dragon_choices[5]:
            print(cp.wild_dragon_choices[5])

        if wild_dragon == cp.wild_dragon_choices[6]:
            print(cp.wild_dragon_choices[6])

        if wild_dragon == cp.wild_dragon_choices[7]:
            print(cp.wild_dragon_choices[7])

        if wild_dragon == cp.wild_dragon_choices[8]:
            print(cp.wild_dragon_choices[8])

        if wild_dragon == cp.wild_dragon_choices[9]:
            print(cp.wild_dragon_choices[9])

        if wild_dragon == cp.wild_dragon_choices[10]:
            print(cp.wild_dragon_choices[10])

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
                misc.player_dragon_stats["HP:"] = misc.player_dragon_stats["HP:"] + 1
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_berries()

            if wild_berries == cp.wild_berry_choices[4]:
                print(cp.wild_berry_choices[4])
                misc.player_dragon_stats["HP:"] = misc.player_dragon_stats["HP:"] + 3
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_berries()

            if wild_berries == cp.wild_berry_choices[5]:
                print(cp.wild_berry_choices[5])
                misc.player_dragon_stats["HP:"] = misc.player_dragon_stats["HP:"] + 5
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_berries()

            if wild_berries == cp.wild_berry_choices[6]:
                print(cp.wild_berry_choices[6])
                misc.player_dragon_stats["HP:"] = misc.player_dragon_stats["HP:"] - 5
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_berries()

        elif eat_wild_berries == "no":
            print(cp.filler_dialogue[3])
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
                misc.player_dragon_stats["HP:"] = misc.player_dragon_stats["HP:"] + 1
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_elixir()

            if elixir == cp.elixir_choices[4]:
                print(cp.elixir_choices[4])
                misc.player_dragon_stats["HP:"] = misc.player_dragon_stats["HP:"] + 3
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_elixir()

            if elixir == cp.elixir_choices[5]:
                print(cp.elixir_choices[5])
                misc.player_dragon_stats["HP:"] = misc.player_dragon_stats["HP:"] + 5
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_elixir()

            if elixir == cp.elixir_choices[6]:
                print(cp.elixir_choices[6])
                misc.player_dragon_stats["HP:"] = misc.player_dragon_stats["HP:"] - 5
                DragonUpgrades.dragon_check_health()
                ChoicePrompts.view_stats_elixir()

        elif drink_elixir == "no":
            print(cp.filler_dialogue[3])
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
                    PlayerMoveChoices2.player_move_options()
                elif exit_dark_cave == "no":
                    print("\nFor stalling inside the cave, a set of spiked rocks split you and your dragon in half.")
                    print("You both die. You lose. Goodbye.")
                    quit()
                else:
                    print(exit_dark_cave)

        elif enter_dark_cave == "no":
            print(cp.filler_dialogue[3])
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
            for x, y in misc.player_dragon_stats.items():
                print(x, y)
            PlayerMoveChoices2.player_move_options()
        elif stats == "a":
            for x, y in misc.player_dragon_attacks.items():
                print(x, y)
            PlayerMoveChoices2.player_move_options()
        elif stats == "s":
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
            for x, y in misc.player_dragon_stats.items():
                print(x, y)
            PlayerMoveChoices2.player_move_options()
        elif stats == "a":
            for x, y in misc.player_dragon_attacks.items():
                print(x, y)
            PlayerMoveChoices2.player_move_options()
        elif stats == "s":
            PlayerMoveChoices2.player_move_options()
        else:
            print(limits.choice_restriction5)
            ChoicePrompts.view_stats_berries()
