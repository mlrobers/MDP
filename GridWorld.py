from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    FORWARD = 4
    RIGHT = 5
    BACKWARD = 6
    LEFT = 7

states = []
for i in range(3):
    for j in range(4):
        states.append((i+1,j+1))

def actions(state):
    listOfActions = []
    i = state[0]
    j = state[1]

    if (i+1,j) in states: listOfActions.append(Direction.SOUTH)
    if (i-1,j) in states: listOfActions.append(Direction.NORTH)
    if (i,j+1) in states: listOfActions.append(Direction.EAST)
    if (i,j-1) in states: listOfActions.append(Direction.WEST)

    return listOfActions