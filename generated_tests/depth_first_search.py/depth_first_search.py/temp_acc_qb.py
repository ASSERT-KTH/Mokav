def patched_func(node_dict, startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        elif node == goalnode:
            return True
        else:
            nodesvisited.add(node)
            return any(
                search_from(nextnode) for nextnode in node_dict[node]['successors']
            )

    return search_from(startnode)
