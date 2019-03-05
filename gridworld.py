from mdp import *

r = -0.04
y = 1
e = 0.1

finish_line_spaces = []
pits = []
terminals = []

def maze_builder(maze_string):
    state_space = list()
    i = 1
    j = 1
    for char in maze_string:
        if char == "O":
            state_space.append((i, j))
            j += 1
            continue
        if char == "x":
            state_space.append((i, j))
            pits.append((i, j))
            terminals.append((i, j))
            j += 1
            continue
        if char == "f":
            state_space.append((i, j))
            finish_line_spaces.append((i, j))
            terminals.append((i, j))
            j += 1
            continue
        if char == "*":
            j += 1
            continue
        if char == "\n":
            i += 1
            j = 1
            continue

    return state_space

def left(direction):
    return {Direction.NORTH : Direction.WEST,
            Direction.EAST : Direction.NORTH,
            Direction.SOUTH : Direction.EAST,
            Direction.WEST : Direction.SOUTH}[direction]


def right(direction):
    return {Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH}[direction]


def forward(direction):
    return direction


def is_terminal(state):
    if state in terminals:
        return True
    else:
        return False


def actions(state):
    return [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]


def result(state, action):
    i = state[0]
    j = state[1]

    if action == Direction.NORTH: i -= 1
    if action == Direction.SOUTH: i += 1
    if action == Direction.EAST: j += 1
    if action == Direction.WEST: j -= 1

    if (i, j) in state_space:
        return (i, j)
    else:
        return state

def successors(state):
    successors = set()
    for action in actions(state):
        successors.add(result(state, action))

    return list(successors)


def transition_model(state, action, next_state):
    p = 0

    if result(state, forward(action)) == next_state: p += 0.8
    if result(state, left(action)) == next_state: p += .1
    if result(state, right(action)) == next_state: p += .1

    return p


def rewards(state):
    if state in finish_line_spaces: return 1
    if state in pits: return -1

    return r

maze1 = "Ox*xf*f\n" \
        "Of*xO*O\n" \
        "O**OO*x\n" \
        "OO*O**O\n" \
        "OOOOOOO\n" \
        "OO*****\n" \
        "OOOOOOx\n" \
        "OO***f*\n"

maze2 = "OOOf\n"\
        "O*Ox\n"\
        "OOOO\n"

state_space = maze_builder(maze2)

grid_world = MDP(state_space, actions, transition_model, rewards, y)
grid_world.get_successors = successors
grid_world.is_terminal_state = is_terminal

grid_world.value_iteration(e)

print()

policies = dict()

for state in state_space:
    policies[state] = grid_world.optimal_policy(state)

print()
print("Utilities:")
for thing in grid_world.u.items():
    print(thing)

print()
print("Policies: (r = %.3f)" % r)
print(grid_world)