import math
import copy
#Yarelit Mendoza and Travis Chamness :)
game = [1,2,5,2]
treeDepth = math.log(len(game), 2)


# function gets successors for current node
def getSuccessors(state):
    if len(state) > 1:
        child = copy.deepcopy(state)
        return [child[1:len(child)], child[0:len(child)-1]]
    else:
        return state

#tests successors
print("Parent node: ", game)
successors = getSuccessors(game)
print("Children: ", successors)

print("\nParent node: ", successors[0])
a = getSuccessors(successors[0])
print("Children: ", a)

print("\nParent node: ", a[0])
a2 = getSuccessors(a [0])
print("Children: ", a2)

def isTerminal(node):
    if len(node) == 1:
        return True

# def value(state):
# if the state is a terminal state: return the state's utility
# if the next agent is MAX: return max-value(state)
# if the next agent is MIN: return min-value(state)

def value(state, maxTurn):
    if isTerminal(state):
        return state[0]

    if maxTurn:
        return maxValue(state)
    else:
        return minValue(state)


# def max-value(state):
# initialize v = -inf
# for each successor of state:
# v = max(v, value(successor))
# return v

def maxValue(state):
    v = -math.inf
    successor = getSuccessors(state)

    for i in range(len(successor)):
         v = max(v, value(successor, False))
    return v

print(maxValue(a2[0]))

# def min-value(state):
# initialize v = +inf
# for each successor of state:
# v = min(v, value(successor))
# return v

def minValue(state):
    v = math.inf
    successor =  getSuccessors(state)

    for i in range(len(successor)):
        v = min(v, value(successor, True))
    return v
    
value(game, True)