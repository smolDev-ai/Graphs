from util import Stack

# strokesRequired takes in the canvas (matrix) as an argument

# Each cluster of letters in this canvas is a continuous stroke that our
# painter can paint (nodes)

# the letters cannot be diagonal from each other, similar to the island
# problem.

# what are the differences between this and the island problem?
# we're checking for more than just one value. 
    # a, b, c instead of just 1
    # this changes something, but I"m not super sure what.



def strokes_required(canvas):
    # Need to create our visited matrix.
    # should be a matrix of False for the length
    # of the canvas

    # we also need a stroke counter

    visited = []

    for i in range(len(canvas)):
        visited.append([False] * len(canvas))
    stroke_count = 0

    def get_neighbors(row, col, canvas):
        neighbors = []

        # need to figure out a good way to check
        # for the different letters
        pass

    def depth(starting_vertex, end_vertex, canvas, visited):
        stack = Stack()
        stack.push((starting_vertex, end_vertex))

        while stack.size > 0:
            coords = stack.pop()
            row = coords[0]
            col = coords[1]

            if not visited[row][col]:
                # flip the visited matrix here to true
                visited[row][col] = True

                for node in get_neighbors(row, col, canvas):
                    stack.push(node)
        
        return visited



    # From here we need to loop over the matrix and get the columns and
    # the rows similar to the island problem.
    
    # If, while we're moving through nodes, we come across one that isn't
    # already in visited, we need to add it.
    # We also need to get the nodes adjacent to it in the cardinal directions.
    # I think Brady did something like:
    # row - 1 for north
    # row + 1 for south
    # col + 1 for east
    # col - 1 for west

    # expected value is a number
    pass


print(strokes_required([
['a', 'a', 'a', 'b', 'a'],
['a', 'b', 'a', 'b', 'a'],
['a', 'a', 'a', 'c', 'a'],
]))
