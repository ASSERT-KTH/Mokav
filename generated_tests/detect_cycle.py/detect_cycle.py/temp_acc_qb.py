# def patched_func(node):
#     hare = tortoise = node

#     while True:
#         if hare is None or hare.successor is None:
#             return False

#         tortoise = tortoise.successor
#         hare = hare.successor.successor

#         if hare is tortoise:
#             return True


def patched_func(node_dict, start_node):
    hare = tortoise = start_node

    while True:
        if hare is None or node_dict[hare]['successor'] is None:
            return False

        tortoise = node_dict[tortoise]['successor']
        hare = node_dict[node_dict[hare]['successor']]['successor']

        if hare is tortoise:
            return True



"""
def detect_cycle(node):
    hare = tortoise = node

    while True:
        if hare.successor is None or hare.successor.successor is None:
            return False

        tortoise = tortoise.successor
        hare = hare.successor.successor

        if hare is tortoise:
            return True
"""
