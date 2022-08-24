import game_input_limits as limits
import numpy as np
import choice_prompts as cp
import opponent_variables as ov
import player_variables as pv


class DragonDuels:
    """
    Overview:

    Usage:
    """
    @staticmethod
    def trainer_dragon_duels():
        duel_dragon = input("\nWould you like to duel the trainer's dragon? (yes/no)\n")

        if duel_dragon == "yes":
            print(cp.filler_dialogue[7])
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
            print(cp.filler_dialogue[7])
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
        print("\nWhat would you like to do?")
        DragonAttributesAndUpgrades.list_player_dragon_attacks()
        DragonDuels.view_stats_trainer_dragon()

        battle = input("\n>>> ")
        if battle == "a":

        if battle == "b":

        if battle == "c":

        if battle == "d":

        else:
            print(limits.choice_restriction1)
            DragonDuels.trainer_dragon_battle()

    @staticmethod
    def wild_dragon_battle():
        battle = input("\nWhat would you like to do?")
        DragonAttributesAndUpgrades.list_player_dragon_attacks()
        DragonDuels.view_stats_trainer_dragon()

    @staticmethod
    def view_stats_trainer_dragon():
        print("\nHit 'X' to view your dragon's stats")
        print("\nHit 'A' to view your dragon's attacks")
        print("\nHit 'S' to skip and continue")

        stats = input("\n>>> ")
        if stats == "x":
            for x, y in pv.player_dragon_stats.items():
                print(x, y)
            DragonDuels.trainer_dragon_battle()
        elif stats == "a":
            for x, y in pv.player_dragon_attacks.items():
                print(x, y)
            DragonDuels.trainer_dragon_battle()
        elif stats == "s":
            DragonDuels.trainer_dragon_battle()
        else:
            print(limits.choice_restriction1)
            DragonDuels.view_stats_trainer_dragon()

    @staticmethod
    def view_stats_wild_dragon():
        print("\nHit 'X' to view your dragon's stats")
        print("\nHit 'A' to view your dragon's attacks")
        print("\nHit 'S' to skip and continue")

        stats = input("\n>>> ")
        if stats == "x":
            for x, y in pv.player_dragon_stats.items():
                print(x, y)
            DragonDuels.wild_dragon_battle()
        elif stats == "a":
            for x, y in pv.player_dragon_attacks.items():
                print(x, y)
            DragonDuels.wild_dragon_battle()
        elif stats == "s":
            DragonDuels.wild_dragon_battle()
        else:
            print(limits.choice_restriction1)
            DragonDuels.view_stats_wild_dragon()


class DragonAttributesAndUpgrades:
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

    @staticmethod
    def list_player_dragon_attacks():
        if pv.player_dragon_stats["Dragon Element:"] == "Fire":
            if pv.player_dragon_stats["Level:"] == 1:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: Dodge")

            if pv.player_dragon_stats["Level:"] == 2:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: Dodge")

            if pv.player_dragon_stats["Level:"] == 3:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: Dodge")

            if pv.player_dragon_stats["Level:"] == 4:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: {}".format(pv.player_dragon_attacks["Special Attack:"]))
                print("D: Dodge")

            if pv.player_dragon_stats["Level:"] == 5:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: {}".format(pv.player_dragon_attacks["Special Attack:"]))
                print("D: Dodge")

        if pv.player_dragon_stats["Dragon Element:"] == "Water":
            if pv.player_dragon_stats["Level:"] == 1:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: Dodge")

            if pv.player_dragon_stats["Level:"] == 2:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: Dodge")

            if pv.player_dragon_stats["Level:"] == 3:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: Dodge")

            if pv.player_dragon_stats["Level:"] == 4:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: {}".format(pv.player_dragon_attacks["Special Attack:"]))
                print("D: Dodge")

            if pv.player_dragon_stats["Level:"] == 5:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: {}".format(pv.player_dragon_attacks["Special Attack:"]))
                print("D: Dodge")

        if pv.player_dragon_stats["Dragon Element:"] == "Earth":
            if pv.player_dragon_stats["Level:"] == 1:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: Dodge")

            if pv.player_dragon_stats["Level:"] == 2:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: Dodge")

            if pv.player_dragon_stats["Level:"] == 3:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: Dodge")

            if pv.player_dragon_stats["Level:"] == 4:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: {}".format(pv.player_dragon_attacks["Special Attack:"]))
                print("D: Dodge")

            if pv.player_dragon_stats["Level:"] == 5:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: {}".format(pv.player_dragon_attacks["Special Attack:"]))
                print("D: Dodge")

        if pv.player_dragon_stats["Dragon Element:"] == "Air":
            if pv.player_dragon_stats["Level:"] == 1:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: Dodge")

            if pv.player_dragon_stats["Level:"] == 2:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: Dodge")

            if pv.player_dragon_stats["Level:"] == 3:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: Dodge")

            if pv.player_dragon_stats["Level:"] == 4:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: {}".format(pv.player_dragon_attacks["Special Attack:"]))
                print("D: Dodge")

            if pv.player_dragon_stats["Level:"] == 5:
                print("A: {}".format(pv.player_dragon_attacks["Attack 1:"]))
                print("B: {}".format(pv.player_dragon_attacks["Attack 2:"]))
                print("C: {}".format(pv.player_dragon_attacks["Special Attack:"]))
                print("D: Dodge")
