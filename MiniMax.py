#Authored by Yarelit Mendoza and Travis Chamness
import math

class Node:
    def __init__(self, value_list):
        self.parent = None
        self.children = []
        self.utility = 0
        self.value_list
        #If Agent is True, then Maximizer, else minimizer
        self.agent = True
        
def value(value_list, node):
    # If the value_list is empty
    if not value_list:
        return node.utility
    if node.agent:
        return max_value(node)
    if not node.agent:
        return min_value(node)

def max_value(node):
    utility = -math.inf

def min_value(node):
    utility = math.inf


# Minimax performs the minimax algorithm. 
# Parameter value_list: expected to come in the form of a python list of numbers
def minimax(value_list):
    root_node = Node()
    value(value_list, root_node)