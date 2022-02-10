""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    min = -1000
    max = 100000
    return checkMinMax(root, min, max)
    
def checkMinMax(root, min, max):
    if root is None:
        return True
    if root.data <= min or root.data >= max:
        return False
    return (checkMinMax(root.left, min, root.data) and checkMinMax(root.right, root.data, max))
