# This file contains all probabilities for all prompts.
# Ex: Probabilities of what happens when you face dragons, trainers, caves, etc.

import numpy as np
import choice_prompts as cp


trainer_choices_prob = np.random.choice(cp.trainer_choices, p=[0.7, 0.25, 0.05])

trainer_dragon_prob = np.random.choice(cp.trainer_dragon_choices, p=[0.125, 0.049, 0.225, 0.1, 0.001, 0.125, 0.049,
                                                                     0.225, 0.1, 0.001])

game_continuation_prob = np.random.choice(cp.game_continuity_choices, p=[0.14, 0.18, 0.18, 0.18, 0.18, 1.4])

wild_dragon_prob = np.random.choice(cp.wild_dragon_choices, p=[0.125, 0.049, 0.225, 0.06, 0.001, 0.125, 0.049, 0.225,
                                                               0.06, 0.001, 0.08])

wild_berry_prob = np.random.choice(cp.wild_berry_choices, p=[0.05, 0.1, 0.05, 0.05, 0.25, 0.15, 0.15, 0.1, 0.1])

boulder_prob = np.random.choice(cp.boulder_choices, p=[0.5, 0.2, 0.2, 0.1])

dark_cave_prob = np.random.choice(cp.dark_cave_choices, p=[0.2, 0.2, 0.2, 0.2, 0.2])

elixir_prob = np.random.choice(cp.elixir_choices, p=[0.05, 0.1, 0.05, 0.05, 0.25, 0.15, 0.15, 0.1, 0.1])
