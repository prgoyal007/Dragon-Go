# Contains all possible prompt options from possible encounters
# Ex: trainers, wild dragons, wild berries, etc.
#
# These are all randomly generated through probabilities (maybe)
# After called upon, all possibilities must be printed and stated
# if something == something
#   print(something[0])


filler_dialogue = (
    "\nNo worries. Maybe next time you'll face another trainer.",
    "\nDamn, missed an easy duel. Maybe next time you'll face another wild dragon.",
    "\nHow unfortunate...your dragon just died. You lose. Goodbye.",
    "\nOkay, that's lame but it's fine.",
    "\nPhew! That was a close one.",
    "\nHow unfortunate...you just died. You lose. Goodbye.",
    "\nHow unfortunate...both you AND your dragon die. You lose. Goodbye.",
    "\nAh you like a challenge don't ya?"
)


trainer_choices = (
    "\nThe trainer sees you with your dragon as a threat, and summons their dragon.",
    "\nThe trainer sees you with your dragon and leaves in search of better challenges.",
    "\nThe trainer sees you with your dragon and flees out of fear."
)

trainer_dragon_choices = (
    "\nThe trainer summons their level 2 Fire Dragon",
    "\nThe trainer summons their level 4 Fire Dragon",
    "\nThe trainer summons their level 1 Water Dragon",
    "\nThe trainer summons their level 3 Water Dragon",
    "\nThe trainer summons their level 5 Water Dragon",
    "\nThe trainer summons their level 2 Earth Dragon",
    "\nThe trainer summons their level 4 Earth Dragon",
    "\nThe trainer summons their level 1 Air Dragon",
    "\nThe trainer summons their level 3 Air Dragon",
    "\nThe trainer summons their level 5 Air Dragon",
)

game_continuity_choices = (
    "\nYou find some wild berries.",
    "\nA boulder is heading towards you.",
    "\nYou run into another trainer.",
    "\nYou run into a wild dragon.",
    "\nYou approach a dark cave.",
    "\nYou find a bottle of elixir."
)

wild_dragon_choices = (
    "\nYou approach the wild dragon to learn that it's a level 1 Fire dragon.",
    "\nYou approach the wild dragon to learn that it's a level 3 Fire dragon.",
    "\nYou approach the wild dragon to learn that it's a level 5 Fire dragon.",
    "\nYou approach the wild dragon to learn that it's a level 2 Water dragon.",
    "\nYou approach the wild dragon to learn that it's a level 4 Water dragon.",
    "\nYou approach the wild dragon to learn that it's a level 1 Earth dragon.",
    "\nYou approach the wild dragon to learn that it's a level 3 Earth dragon.",
    "\nYou approach the wild dragon to learn that it's a level 5 Earth dragon.",
    "\nYou approach the wild dragon to learn that it's a level 2 Air dragon.",
    "\nYou approach the wild dragon to learn that it's a level 4 Air dragon.",
    "\nThe wild dragon flees before you could reach it."
)

wild_berry_choices = (
    "\nYour dragon eats the wild berries and the berries kill your dragon.",
    "\nYour dragon eats the wild berries and the berries regenerate your dragon to full health!",
    "\nYour dragon eats the wild berries and the berries upgrades your dragon to the next level!",
    "\nYour dragon eats the wild berries and the berries increases your dragon's health by 1 point!",
    "\nYour dragon eats the wild berries and the berries increases your dragon's health by 3 points!",
    "\nYour dragon eats the wild berries and the berries increases your dragon's health by 5 points!",
    "\nYour dragon eats the wild berries and the berries decreases your dragon's health by 5 points."
)

elixir_choices = (
    "\nYour dragon drinks the bottle of elixir and the elixir kills your dragon.",
    "\nYour dragon drinks the bottle of elixir and the elixir regenerates your dragon to full health!",
    "\nYour dragon drinks the bottle of elixir and the elixir upgrades your dragon to the next level!",
    "\nYour dragon drinks the bottle of elixir and the elixir increases your dragon's health by 1 point!",
    "\nYour dragon drinks the bottle of elixir and the elixir increases your dragon's health by 3 points!",
    "\nYour dragon drinks the bottle of elixir and the elixir increases your dragon's health by 5 points!",
    "\nYour dragon drinks the bottle of elixir and the elixir decreases your dragon's health by 5 points."
)

dark_cave_choices = (
    "\nYou enter the dark cave to find a wild dragon.",
    "\nYou enter the dark cave to find wild berries.",
    "\nYou enter the dark cave to find a bottle of elixir.",
    "\nYou enter the dark cave to find a deadly trap. The trap unfortunately kills you and your dragon.",
    "\nYou enter the dark cave to find nothing. But you see a clear exit out of the dark cave."
)

boulder_choices = (
    "\nYou try to dodge the boulder and luckily you and your dragon dodge it just in time.",
    "\nYou try to dodge the boulder and luckily you dodge it, but your dragon fails to dodge it and dies.",
    "\nYou try to dodge the boulder and luckily your dragon dodges it, but you fail to dodge it and die.",
    "\nYou try to dodge the boulder and unfortunately you and dragon fail to dodge it and die."
)

trainer_dragon_escape_choices = (
    "\nYou tried to escape the trainer and his dragon, and you successfully escaped!"
    "\nYou tried to escape the trainer and his dragon, and unfortunately you couldn't escape."
    "Now you have to duel with them."
)

wild_dragon_escape_choices = (
    "\nYou tried to escape the wild dragon, and you successfully escaped!"
    "\nYou tried to escape the wild dragon, and unfortunately you couldn't escape."
    "Now you have to duel with them."
)
