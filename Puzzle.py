"""
Homework 8: Graph Algorithms – II

Name:       Marcos Valdez
ONID:       valdemar

Course:     CS 325
Section:    400
Term:       Winter 2023

Edited:     03/06/2023
Due:        03/06/2023

Description: Submission for homework problem 3.
             Function that uses a queue implementation of BFS to find
             and return the shortest path from a source to a destination
             on a board.

Note:        Extra credit (problem 3d) implemented.
"""


from collections import deque
from copy import  deepcopy


def solve_puzzle(Board: list[list[str]], Source: tuple[int],
                 Destination: tuple[int]) -> list[tuple[int]]:
    """
    Determines a shortest path from Source to Destination on Board
    using a queue based BFS. Valid moves are to adjacent, traversable
    spaces (see Board param). Graph of board is unweighted; all moves
    have a cost of 1.

    :param Board:   list of list of strings representing a 2D puzzle board.
                    Outer list represents rows, inner list represents
                    columns, and strings respresent spaces. All strings
                    must be '-' or '#' where '-' is traversable and '#'
                    is blocked.
    :param Source:      tuple of two ints representing the indexed address
                        of the starting space
    :param Destination: tuple of two ints representing the indexed address
                        of the goal space

    :return: tuple in which
                first element:  list of tuples of two ints representing the
                                shortest path in terms of the space addresses
                                in order
                second element: string consisting of letters from 'RDLU'
                                representing the shortest path in terms of
                                directions taken in order
    """

    # Reject clearly unsolvable inputs
    if Board[Source[0]][Source[1]] == '#' or \
            Board[Destination[0]][Destination[1]] == '#':
        return

    # Track visited cells and mark Source as visited
    rows = len(Board)
    cols = len(Board[0])
    visited = [[False for i in range(cols)] for j in range(rows)]
    visited[Source[0]][Source[1]] = True

    # Create queue for tracking paths
    bfsQueue = deque()
    numPath = [Source]          # list of cell coordinates in path
    dirPath = ''                # string of directions in path
    start = (numPath, dirPath)
    bfsQueue.append(start)

    # Perform BFS
    while bfsQueue:
        path = bfsQueue.popleft()
        cell = path[0][len(path[0])-1]

        if cell == Destination:
            # Path found; return path in both formats
            return path[0], path[1]

        # Evaluate candidate directions
        for nextDir in 'RDLU':
            row = cell[0]
            col = cell[1]

            if nextDir == 'R':
                col += 1
            elif nextDir == 'D':
                row += 1
            elif nextDir == 'L':
                col -= 1
            else:
                row -= 1

            if row >= 0 and row < rows and col >= 0 and col < cols and \
                    Board[row][col] == '-' and not visited[row][col]:
                # Candidate cell is on board, not #, and not visited
                visited[row][col] = True

                numPath = deepcopy(path[0])
                numPath.append((row, col))

                dirPath = deepcopy(path[1])
                dirPath += nextDir

                # Enqueue path
                nextPath = numPath, dirPath
                bfsQueue.append(nextPath)

    # No path found; return None


if __name__ == "__main__":
    """
    Test script
    """
    puzzle = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
    ]

    paths = (
        ((0, 2), (2, 2)),
        ((0, 0), (4, 4)),
        ((0, 0), (4, 0))
    )

    for path in paths:
        """
        Expected output:
        ([(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], 'LDDR')
        ([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], 'RRRRDDDD')
        None
        """
        print(solve_puzzle(puzzle, path[0], path[1]))
