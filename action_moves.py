# All choices for going forward, backward, left, and right.
# These values are going to be randomly generated once called upon
#
# Forward, left, and right all have same options, but all will have different probabilities assigned
# This is to lessen the probabilities of getting two or more of the same prompt
#
# Need to find way to make sure the same 2 or more probabilities don't show up
# Google python code for that

forward_left_right_options = ("You see a trainer.",
                              "You see a path heading further into Vrubel.",
                              "You see a wild dragon.",
                              "You see some wild berries.",
                              "You see a bottle of elixir.",
                              "You see a dark cave.",
                              "You see a boulder heading towards you."
                              )

backward_options = ("You exit the entrance of Vrubel.",
                    "You go back to your earlier position."
                    )

forward_left_right_continuity = ("You approach the trainer.",
                                 "You head further into Vrubel.",
                                 )