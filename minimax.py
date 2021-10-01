import math
import copy
#Yarelit Mendoza and Travis Chamness :)
game = [1,2,5,2]

# function gets successors for current node
def getSuccessors(state):
    if len(state) == 1:
        return None
    else:
        child = copy.deepcopy(state)
        return [child[1:len(child)], child[0:len(child)-1]]

#tests successors
print("Parent node: ", game)
successors = getSuccessors(game)
print("Children: ", successors)

print("\nParent node: ", successors[0])
a = getSuccessors(successors[0])
print("Children: ", a)

# def value(state):
# if the state is a terminal state: return the state's utility
# if the next agent is MAX: return nax-value(state)
# if the next agent is MIN: return min-value(state)

def value(state):
    return None

# def max-value(state):
# initialize v = -inf
# for each successor of state:
# v = max(v, value(successor))
# return v

def maxValue(state):
    v = -math.inf

# def min-value(state):
# initialize v = +inf
# for each successor of state:
# v = min(v, value(successor))
# return v

def minValue(state):
    v = math.inf
    