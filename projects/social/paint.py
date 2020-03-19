from util import Stack

# strokesRequired takes in the canvas (matrix) as an argument

# Each cluster of letters in this canvas is a continuous stroke that our
# painter can paint (nodes)

# the letters cannot be diagonal from each other, similar to the island
# problem.

# what are the differences between this and the island problem?
# we're checking for more than just one value. 
    # a, b, c instead of just 1
    # this changes something, but I'm not super sure what.


def strokes_required(canvas):
    def get_neighbors(row, col, canvas, string):
        neighbors = []

        # need to figure out a good way to check
        # for the different letters

        # We need to get the nodes adjacent to it in the cardinal directions.
        # I think Brady did something like:
        # row - 1 for north
        # row + 1 for south
        # col + 1 for east
        # col - 1 for west

        # print(f"canvas in get_neighbors: {canvas[row][col]}\n nodes: {row},{col}")

        if row > 0 and canvas[row-1][col] == string:
            neighbors.append((row-1, col))
        if row < len(canvas) - 1 and canvas[row+1][col] == string:
            neighbors.append((row+1, col))
        if col < len(canvas[0]) - 1 and canvas[row][col+1] == string:
            neighbors.append((row, col+1))
        if col > 0 and canvas[row][col-1] == string:
            neighbors.append((row, col-1))
        # print(row, col)
        # print(neighbors, canvas[row][col])
        return neighbors
    
    def depth(starting_vertex, end_vertex, canvas, visited):
        stack = Stack()
        stack.push((starting_vertex, end_vertex))

        while stack.size() > 0:
            coords = stack.pop()
            row = coords[0]
            col = coords[1]
            # print(f"in depth:\n \tcoords: {coords}\n \tvisited: {visited}")

            if not visited[row][col]:
                # flip the visited matrix here to true
                visited[row][col] = True
                for node in get_neighbors(row, col, canvas, canvas[row][col]):
                    stack.push(node)

        return visited
    # Need to create our visited matrix.
    # should be a matrix of False for the length
    # of the canvas

    # we also need a stroke counter
    visited = []

    for i in range(len(canvas)):
        visited.append([False] * len(canvas[0]))
    stroke_count = 0

    # From here we need to loop over the matrix and get the columns and
    # the rows similar to the island problem.
    # If, while we're moving through nodes, we come across one that isn't
    # already in visited, we need to add it.
    for col in range(len(canvas[0])):
        for row in range(len(canvas)):
            # print(row, col) # prints correctly
            # print(f"for loop before if")
            if canvas[row][col] == 'a' or canvas[row][col] == 'b' or canvas[row][col] == 'c':
                if not visited[row][col]:
                    print(f"for loop in if: {visited[row][col]}")
                    visited = depth(row, col, canvas, visited)

                    stroke_count += 1
    # expected value is a number
    return stroke_count









print(strokes_required([
['a', 'a', 'a', 'b', 'a'],
['b', 'b', 'b', 'a', 'b'],
['a', 'a', 'a', 'c', 'a'],
]))
