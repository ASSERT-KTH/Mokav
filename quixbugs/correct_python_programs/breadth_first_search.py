from collections import deque as Queue

def patched_func(node_dict, startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:
        node = queue.popleft()

        if node == goalnode:
            return True
        else:
            successors = node_dict[node]['successors']
            queue.extend(successor for successor in successors if successor not in nodesseen)
            nodesseen.update(successors)

    return False
