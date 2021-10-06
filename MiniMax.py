#Authored by Yarelit Mendoza and Travis Chamness
#Date: Oct 5, 2021
#Minimax implementation for COMP 469 Introduction to AI

import math

#Unsuccessful Agent Branch - If the terminal state is equal or less than zero, the agent does not have a winning score on the branch. 
UNSUCCESSFUL_AGENT_BRANCH = 0
#minimum list size to create a new branch
MINIMUM_LIST_SIZE = 1
#Tracked success state of agent
cumulative_success = False


class Node:
    def __init__(self, value_list):
        #Parent of the state
        self.parent = None
        #Successors of the state
        self.children = []
        #The utility associated to that specific agent/opponent
        self.utility = 0
        #Tracked cumulative sum of the state in the state tree
        self.cumsum = 0
        #Nodes personal state list of values
        self.value_list = value_list
        #If Agent is True, then Maximizer, else minimizer
        self.agent = True
    
    #Produce a hard copy of the node
    def copy(self):
        newNode = Node(self.value_list.copy())
        newNode.parent = self.parent
        newNode.agent = self.agent
        newNode.children = self.children.copy()
        newNode.utility = self.utility
        newNode.cumsum = self.cumsum
        return newNode

#Value Function - Receives the current node and addresses the node as either Agent, Opponent, or Terminal State.
def value(node):
    #The return of this value is not useful in this implementation. Disregard results from Value.
    # What needs to be accounted for is the cummulative success variable which tracks whether
    # any successful paths exist.
    #Terminal State
    if not node.value_list:
        return node.utility 
    #Agent State
    if node.agent:
        return max_value(node)
    #Opponent State
    if not node.agent:
        return min_value(node)

# Successor Helper performs the repetitious work for successor function 
# of assigning appropriate values and cummulative sum for the respective 
# agent or opponent.
def successor_func_helper(node):
    for index, child in enumerate(node.children):
        child.agent = not node.agent
        #Assign parent value
        child.parent = node
        #Accordingly update utility and cumsum
        #If the children are agents
        if child.agent:
            #Left Child
            if index == 0:
                child.utility = -child.value_list.pop(0)
                child.cumsum = child.cumsum + child.utility
            #Right Child
            elif index == 1:
                child.utility = -child.value_list.pop()
                child.cumsum = child.cumsum + child.utility
            #Tertiary Child - Should not exist
            else:
                print("ERROR: Too many children exist")

        #If the children are opponents
        else:
            #Left Child
            if index == 0:
                child.utility = child.value_list.pop(0)
                child.cumsum = child.cumsum + child.utility 
            #Right Child
            elif index ==1:
                child.utility = child.value_list.pop()
                child.cumsum = child.cumsum + child.utility
            #Tertiary Child - Should not exist
            else:
                print("ERROR: Too many children exist")
    return node

def successor_func(node):
    global cumulative_success
    #If more than one value in list of vals exists
    if len(node.value_list) > MINIMUM_LIST_SIZE:
        #Generate children
        left_child = node.copy()
        right_child = node.copy()
        #Assign children to node
        node.children.append(left_child)
        node.children.append(right_child)
        node = successor_func_helper(node)
    #If the value list contains one value
    elif len(node.value_list) == MINIMUM_LIST_SIZE:
        #The child will be a terminal node
        terminal_node = node.copy()
        #Assign terminal node to parent
        node.children.append(terminal_node)
        node = successor_func_helper(node)
        #Cumulative succes determines if at any point a path exists that is a Win for the Agent
        cumulative_success = (cumulative_success or (terminal_node.cumsum > UNSUCCESSFUL_AGENT_BRANCH))
    return node


def max_value(node):
    #Initialize the val to worst case
    val = -math.inf
    #Explore current node successors
    node = successor_func(node)
    #For each successor(child) of the node
    for child in node.children:
        #Calculate the max between the current val and child node
        val = max(val, value(child))
    return val        

def min_value(node):
    #initialize the val to worst case
    val = math.inf
    #Explore current node successors
    node = successor_func(node)
    for child in node.children:
        #Calculate the min between the current val and child node
        val = min(val, value(child))
    return val

# Minimax performs the minimax algorithm. 
# Parameter value_list: expected to come in the form of a python list of numbers
def minimax(value_list):
    global cumulative_success
    #Tracks whether the agent 
    root_node = Node(value_list)
    value(root_node)
    print(cumulative_success)
minimax([1,2,5,2])