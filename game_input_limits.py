# these are acceptable only choices for prompts
yes_no = ["yes", "no"]
choice_restriction1 = "\nUse only lowercase options like 'a' or 'b' etc.\n"
choice_restriction2 = "\nUse only 'yes' or 'no'.\n"
choice_restriction3 = "\nUse only 'forward', 'backward', 'left', 'right', or 'h'\n"

"""
def generate_only_choice(choice_list):
    print("Use only " + ', '.join(choice_list))


generate_only_choice(['a', 'b', 'c', 'd'])
"""
