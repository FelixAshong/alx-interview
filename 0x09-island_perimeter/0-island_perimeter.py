#!/usr/bin/python3
"""
    function def island_perimeter(grid): that returns
    the perimeter of the island described in grid:
"""


def island_perimeter(grid):
    """return the perimeter of the island described in grid"""
    perimeter = 0
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if grid[i][j] == 1:
                perimeter += 4
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
            j += 1
        i += 1
    return perimeter
