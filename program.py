########################################################
#                                                      #
# This program will save the output steps in a txt file#
#                                                      #
########################################################


import copy
import time



goal = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 15, 0)

)
# We will be using deepcopy here.
# We usually think that assignment a variable to another
# creates a new copy of the old variable. But that is not the
# case. While preparing this software I realized that my
# skeleton was failing everytime because even if I assign
# a different variable to my list, it somehow used to get
# altered. That's when I went up on the internet and learned
# about deepcopy.
# A shallow copy never create a copy of NESTED OBJECTS. It
# just copies the reference of nested objects.
# A deep copy does that. Hence we import copy


# Let use create the skeleton of our 4x4 puzzle. The blank box
# will be used as zero in our case instead of an underscore '_'


# Let us find that blank box :

def blank_box_index(state):
    for i in range(4): # 4 since the puzzle is 4x4
        for j in range(4):
            if state[i][j] == 0:
                return i, j

# Our puzzle restricts the blank box to move only
# UP, DOWN, LEFT and RIGHT
# Let us create a function that generates the end state
# when the puzzle has moved UP, DOWN, LEFT and RIGHT


def puzzle_steps(state):
    x,y = blank_box_index(state)
    steps = []
    # Let us take each row of the state individually:
    rows = [list(state[0]), list(state[1]), list(state[2]), list(state[3])]
    # If blank box moves UP:
    if x != 0: # Because it cannot move up if it is at the top
        up = copy.deepcopy(rows)
        up[x-1][y], up[x][y] = up[x][y], up[x-1][y]
        cvt_tuple_up = tuple(
            [
                tuple(up[0]),
                tuple(up[1]),
                tuple(up[2]),
                tuple(up[3])
            ]
        )
        steps.append(cvt_tuple_up)
    # If blank box moves DOWN:
    if x != 3: # Because it cannot move down if its at the bottom
        down = copy.deepcopy(rows)
        down[x+1][y], down[x][y] = down[x][y], down[x+1][y]
        cvt_tuple_down = tuple(
            [
                tuple(down[0]),
                tuple(down[1]),
                tuple(down[2]),
                tuple(down[3])
            ]
        )
        steps.append(cvt_tuple_down)
    # If blank box moves LEFT:

    if y != 0:
        left = copy.deepcopy(rows)
        left[x][y], left[x][y - 1] = left[x][y - 1], left[x][y]
        cvt_tuple_left = tuple(
            [
                tuple(left[0]),
                tuple(left[1]),
                tuple(left[2]),
                tuple(left[3])
            ]
        )
        steps.append(cvt_tuple_left)

    # If blank box moves RIGHT :
    if y != 3: # Since it cannot go right when y is 3
        right = copy.deepcopy(rows)
        right[x][y], right[x][y+1] = right[x][y+1], right[x][y]
        cvt_tuple_right = tuple(
            [
                tuple(right[0]),
                tuple(right[1]),
                tuple(right[2]),
                tuple(right[3])
            ]
        )
        steps.append(cvt_tuple_right)
    return steps #Return the acquired steps

# We need to find the path that will lead us to the goal state
# The best way to do that is do backward search i.e. from goal
# to the initial state. It will save time as we will not be
# using any heuristic

# As mentioned in the hints we were asked to look for different
# data structure and were preferred to use dictionary. It seemed
# plausible to use hash tables as the preferred which can make
# dictionary accessing faster. This is the reason why I have been
# taking the pain to store steps as tuple and not as list.

def path_traversed(initial_state, path):
    list_path_traversed = [goal]
    current_step = goal
    while True: # while True creates an infinite loop, which ends manually
        current_step = path[hash(current_step)]
        list_path_traversed.append(current_step)
        if current_step == initial_state:
            break # This is when we leave the infinite loop
    list_path_traversed.reverse() # Reverse the path calculated
    return list_path_traversed

# As per our assignment requirements we are required to print
# the steps that our agent is taking to find the solution
# The below function is doing the same. Defining it early will
# help in not complicating the __main__ function


def report_answer(state):
    answer = '*******************\n'
    for i in state: # Splits the state
        for j in i : # Takes each number from the above split
            if len(str(j)) == 1: # Let us make 1 to 01, to keep the output clean
                answer += ' 0' + str(j)
            else:
                answer += ' ' + str(j) # The blank space is to ensure that the output is readable
        answer += '\n'
    answer += '*******************\n'
    return answer

# Let us define a function that evaluates the solution puzzle recursively


def solution_finder(state):
    steps = {}
    graph_depth = 0
    state_list = {state}

    while True:
        graph_depth += 1
        forward = set()  # Defines how do we move forward from the current state
        for x in state_list:
            if x == goal:
                return graph_depth, steps
            for child in puzzle_steps(x): # Finds children by moving forward in each direction possible
                forward.add(child)
                if hash(child) not in steps: # if our child is not in steps, then we will add the child
                                             # to forward moves which is added to our state list in the next step
                    steps[hash(child)] = x

            state_list = set(forward)
            # Hence our state list is complete


# Let us solve the puzzle now
def main():
    initial_state = (
        (string_input[0], string_input[1], string_input[2], string_input[3]),
        (string_input[4], string_input[5], string_input[6], string_input[7]),
        (string_input[8], string_input[9], string_input[10], string_input[11]),
        (string_input[12], string_input[13], string_input[14], string_input[15])

    )
    # Let us also see how long it took to solve the puzzle

    start = time.time()
    depth, result = solution_finder(initial_state)
    stop = time.time()
    time_elapsed = stop - start
    _file = open(file_name+".txt", 'w')
    process_details = 'Time elapsed: '+ str(time_elapsed) + 's\n               where s = seconds.\n               ='+str(time_elapsed)[3]+ '.'+ str(time_elapsed)[4:7]+'ms\nDepth of the tree/graph:'+str(depth)+'\nSteps:\n'
    path = path_traversed(initial_state, result)
    counter = 0
    for each_state in path:
        if counter == 0:
            process_details += "Input State: \n"
        else:
            process_details += "Step " + str(counter) + ": \n"
        process_details += report_answer(each_state)
        counter = counter + 1
    _file.write(str(process_details))


string_input = list()
print("Please enter the puzzle in sequential order separated by commas:\n")
user_input = str(input())
string_input = list()
string_input = user_input.split(',')
string_input = list(map(int, string_input))
print("Please enter the name of your output file (without extension):\n")
file_name = str(input())



if len(string_input) == 16:
    main()
    print("The output will be saved in " + file_name + ".txt file in the root folder\n")

else:
    print("Error in input!!!\nPlease try again.")


