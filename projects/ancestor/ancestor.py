from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    # start by building a graph
    # spec says furthest away so depth-first?
    # search because we don't want to hit all nodes

    # can you create a function inside another function?

    # need to change up get neighbors to work with the fact we don't actually have a graph class
    #
    def get_neighbors(node_id):
        # need to take the node_id
        # see if it has any neighbors
        # ancestors is a list of tuples
        # we want to check if the node is in ancestors
        # if it is what do we do?
        neighbors = []

        for parent, child in ancestors:
            if child == node_id:
                neighbors.append(parent)
        
                # print(neighbors)
    
        return neighbors



        # ex: return node_id

    # create DFS
    stack = Stack()
    visited = set()
    current_parent = None

    path_length = 1

    stack.push([starting_node])

    while stack.size() > 0:
        current_path = stack.pop()
        current_node = current_path[-1]



        # find length of current path
        # compare path lengths between loops
        # If it's the longer of the two store it
        # come into loop update path_length if current is bigger
        # update the parent that is the last node in the new longest path
        if path_length < len(current_path):
            path_length = len(current_path)
            current_parent = current_node
            # print(current_parent)
        if path_length == len(current_path) and current_parent:
            # if they're the same length update parent with the smallest value parent
            if current_parent > current_node:
                # print(current_parent)
                current_parent = current_node

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in get_neighbors(current_node):
                stack.push([*current_path, neighbor])
            
    if current_parent:
        return current_parent

    return -1

