def patched_func(node_dict):
    ordered_nodes = [node for node in node_dict if not node_dict[node]['incoming_nodes']]

    for node in ordered_nodes:
        for nextnode in node_dict[node]['outgoing_nodes']:
            if set(ordered_nodes).issuperset(node_dict[nextnode]['incoming_nodes']) and nextnode not in ordered_nodes:
                ordered_nodes.append(nextnode)

    return ordered_nodes
