import random
import action_moves as am


# Use good function name
def foo():
    while True:
        a = ''.join((random.sample(am.forward_left_right_options, 1)))
        b = ''.join((random.sample(am.forward_left_right_options, 1)))
        c = ''.join((random.sample(am.forward_left_right_options, 1)))

        d = (random.sample(am.forward_left_right_options, 1))
        e = (random.sample(am.forward_left_right_options, 1))

        temp_list = [a, b, c]
        my_set = set(temp_list)

        if len(my_set) == len(temp_list):
            foo.new_list = list(my_set)
            return foo.new_list

        elif len(my_set) < len(temp_list):
            my_set.update(d)

            if len(my_set) == 3:
                foo.new_list = list(my_set)
                return foo.new_list

            if len(my_set) < 3:
                my_set.update(e)
                foo.new_list = list(my_set)
                return foo.new_list

        else:
            foo()


def foo_2():
    print("Forward: ", foo.new_list[0])
    print("Backward: ", am.backward_options[0])
    print("Left: ", foo.new_list[1])
    print("Right: ", foo.new_list[2])


foo()
foo_2()
