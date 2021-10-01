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

def isTerminal(node):
    if type(node) == int:
        return True

# def value(state):
# if the state is a terminal state: return the state's utility
# if the next agent is MAX: return max-value(state)
# if the next agent is MIN: return min-value(state)

def value(state, maxTurn):
    if isTerminal(state):
        print("In terminal state aka this is the value: ", state)
        return state

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
    print("Max state:", state)
    v = -math.inf
    successor = getSuccessors(state)

    for i in range(len(successor)):
         v = max(v, value(successor[i], False))
    print("Max value: ", v)
    return v



# def min-value(state):
# initialize v = +inf
# for each successor of state:
# v = min(v, value(successor))
# return v

def minValue(state):
    print("Min state:", state)
    v = math.inf
    successor =  getSuccessors(state)

    for i in range(len(successor)):
        v = min(v, value(successor[i], True))
    print("Min value:", v)
    return v
    
value(game, True)