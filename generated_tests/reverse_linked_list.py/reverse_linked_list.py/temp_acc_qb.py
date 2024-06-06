def patched_func(node_dict, startnode):
    prevnode = None
    node = startnode
    while node:
        nextnode = node_dict[node]['successor']
        node_dict[node]['successor'] = prevnode
        prevnode = node
        node = nextnode
    return prevnode

"""
def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        node.successor = prevnode
        prevnode, node = node, nextnode
    return prevnode

def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        node.successor = prevnode
        node, prevnode = nextnode, node
    return prevnode

"""
