#Authored by Yarelit Mendoza and Travis Chamness
import math

#minimum list size to create a new branch
MINIMUM_LIST_SIZE = 1
#Set of terminal states - May not be necessary
terminal_states = []
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
    
    def copy(self):
        newNode = Node(self.value_list.copy())
        newNode.parent = self.parent
        newNode.agent = self.agent
        newNode.children = self.children.copy()
        newNode.utility = self.utility
        newNode.cumsum = self.cumsum
        return newNode

        
def value(node):
    #The return of this value is not useful in this implementation. Disregard results from Value.
    # What needs to be accounted for is the cummulative success variable which tracks whether
    # any successful paths exist.
    if not node.value_list:
        return node.utility 
    if node.agent:
        return max_value(node)
    if not node.agent:
        return min_value(node)

def successor_func_helper(node):
    for child in node.children:
        child.agent = not node.agent
        #Assign parent value
        child.parent = node
        #Accordingly update utility and cumsum
        #If the children are agents
        if child.agent:
            child.utility = -child.value_list.pop(0)
            child.cumsum = child.cumsum - child.utility
        #If the children are opponents
        else:
            child.utility = child.value_list.pop(0)
            child.cumsum += child.cumsum 
    return node

def successor_func(node):
    global terminal_states
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
        #Add terminal node to terminal list
        terminal_states.append(terminal_node)
        #Cumulative succes determines if at any point a path exists that 
        cumulative_success = (cumulative_success or (terminal_node.cumsum > 0))
    return node


def max_value(node):
    val = -math.inf
    node = successor_func(node)
    for child in node.children:
        val = max(val, value(child))
    #Returning value establishes the tree branching values
    return val        

def min_value(node):
    val = math.inf
    node = successor_func(node)
    for child in node.children:
        val = min(val, value(child))
    #Returning value establishes the tree branching values
    return val

# Minimax performs the minimax algorithm. 
# Parameter value_list: expected to come in the form of a python list of numbers
def minimax(value_list):
    global cumulative_success
    #Tracks whether the agent 
    root_node = Node(value_list)
    print(value(root_node))
    print(cumulative_success)
minimax([1,2,5,2])