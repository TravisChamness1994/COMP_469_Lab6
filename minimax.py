import math
import copy
#Yarelit Mendoza
game = [1,2,5,2]
list = []

# function gets successors for current node :)
def getSuccessors(state):
    if len(state) == 1:
        return None
    else:
        child1 = copy.deepcopy(state)
        child2 = copy.deepcopy(state)
        
        child1.pop(0)
        child2.pop(-1)
        return [child1, child2]

print("Parent node: ", game)
successors = getSuccessors(game)
print("Children: ", successors)

print("\nParent node: ", successors[0])
a = getSuccessors(successors[0])
print("Children: ", a)

print("\nParent node:", a[0])
c = getSuccessors(a[0])
print("Children: ", c)

print("\nParent node:", c[0])
d = getSuccessors(c[0])
print("Children: ", d)

# def value(state):
# if the state is a terminal state: return the state's utility
# if the next agent is MAX: return nax-value(state)
# if the next agent is MIN: return min-value(state)

# def max-value(state):
# initialize v = -inf
# for each successor of state:
# v = max(v, value(successor))
# return v

# def min-value(state):
# initialize v = +inf
# for each successor of state:
# v = min(v, value(successor))
# return v