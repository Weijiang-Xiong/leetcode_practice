from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def make_linked_list(array:List[int]):
    linked_list = [ListNode(array[0])]
    for num in array[1:]:
        new_node = ListNode(num)
        linked_list[-1].next = new_node
        linked_list.append(new_node)
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree_node(array:List[int]):
    
    all_nodes = [TreeNode(val=val) for val in array]
    
    for idx, node in enumerate(all_nodes):
        try:
            node.left = all_nodes[2*idx + 1]
        except:
            node.left = None
        
        try:
            node.right = all_nodes[2*idx+2]
        except:
            node.right = None
            
    return all_nodes[0]
