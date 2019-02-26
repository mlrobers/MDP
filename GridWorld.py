from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


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


states = []
for i in range(3):
    for j in range(4):
        states.append((i+1,j+1))


def actions(state):
    listOfActions = []
    i = state[0]
    j = state[1]

    if (i - 1, j) in states: listOfActions.append(Direction.NORTH)
    if (i, j + 1) in states: listOfActions.append(Direction.EAST)
    if (i + 1, j) in states: listOfActions.append(Direction.SOUTH)
    if (i, j - 1) in states: listOfActions.append(Direction.WEST)

    return listOfActions


