from collections import deque as Queue

def original_func(node_dict, startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while True:
        node = queue.popleft()

        if node == goalnode:
            return True
        else:
            successors = node_dict[node]['successors']
            queue.extend(successor for successor in successors if successor not in nodesseen)
            nodesseen.update(successors)

    return False




"""
Breadth-First Search


Input:
    startnode: A digraph node
    goalnode: A digraph node

Output:
    Whether goalnode is reachable from startnode
"""
