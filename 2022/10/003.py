# DAILY CODING PROBLEM FOR 10/17/2022

# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node: Node, string=""):
    if node == None:
        string += "/ "
        return string

    string += str(node.val) + " "
    string = serialize(node.left, string=string)
    string = serialize(node.right, string=string)
    return string

def deserialize(string, i=0):
    if string[i] == "/":
        if(i < len(string) - 2):
            i += 2
        return None

    else:
        val = string[i:].find(" ") + i
        node = Node(string[i:val])
        node.left = deserialize(string, i = val + 1)
        node.right = deserialize(string, i = val + 1)
        return node

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
