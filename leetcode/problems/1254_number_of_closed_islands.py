'''
========================================
1254. Number of Closed Islands
========================================
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Constraints:
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1

Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],
               [1,0,0,0,0,1,1,0],
               [1,0,1,0,1,1,1,0],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],
               [0,1,0,1,0],
               [0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

========================================
Initial Thoughts
- This is a typical searching problem, where we use depth-first search (DFS) or breadth-first search (BFS) to search from a starting point to all neighboring positions
- But how to determine if a land cell is a part of a closed island or not?
- Here are some different scenarios...
    -- A closed island can have water in the middle of it's body
        1 1 1 1 1
        1 0 0 0 1
        1 0 1 0 1
        1 0 0 0 1
        1 1 1 1 1
    -- A closed island only cares about the 4 cardinals being water, it does not care about the diagonals
        0 1 0
        1 0 1
        0 1 1
    -- A closed island can exist within another closed island
        1 1 1 1 1 1 1
        1 0 0 0 0 0 1
        1 0 1 1 1 0 1
        1 0 1 0 1 0 1
        1 0 1 1 1 0 1
        1 0 0 0 0 0 1
        1 1 1 1 1 1 1
    -- A closed island does not necessarily have a square shape
        1 1 1 1 1 1 1
        1 0 0 0 0 0 1
        1 0 0 0 0 0 1
        1 0 0 0 1 1 1
        1 0 0 0 0 0 1
        1 0 0 0 0 1 1
        1 1 1 1 1 1 1
- Therefore, in order to determine if a land cell is a part of a closed island, we only need to validate that the land cell is not next to the boundary of the grid

========================================
Breadth-First Search Approach
- Essentially, we will look for a land cell that could be part of a closed island we haven't searched already
- Then search all adjacent land cells
- We will assume the land cells are a part of a valid closed island unless we find a land cell on the boundary
- Even if we find a land cell on the boundary, we still want to account for all adjacent cells so they aren't searched again

Algo
- Use an integer to keep track of the number of closed islands found -> closed_islands
- Use a hashset to keep track of land that has already been searched -> visited
- Iterate through grid -> cell
    - If cell is water -> Skip
    - If cell is land and not already visited -> Start BFS
        - Use a boolean to keep track of whether the island has been invalidated -> is_closed
        - Use que to implement the BFS -> que
            - If current cell is on boundary -> is_closed is now False
            - Search in 4 directions
                - If new cell is land and not already visited -> Add to search
- After grid has been searched -> Return closed_islands

Performance
- Let m be the number of rows in grid
- Let n be the number of columns in grid
- Time ->
    -- Iterating grid costs O(m * n)
    -- Performing BFS on the grid can cost up to O(m * n), but using a hashset prevents redundant searches, so the cost is additive
    -- Our operations on the hashset costs O(1)
    -- Overall -> O(m * n)
- Space ->
    -- Using a que can cost up to O(m * n)
    -- Using the hashset can cost up to O(m * n)
    -- Overall -> O(m * n)

========================================
'''

from collections import deque
from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ''' ===== Breadth-First Search ===== '''
        def is_closed_island(start_row, start_col):
            nonlocal visited
            is_closed = True
            que = deque([(start_row, start_col)])
            visited.add((start_row, start_col))

            while que:
                row, col = que.popleft()
                on_boundary = row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1

                if on_boundary:
                    is_closed = False

                for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    is_valid = 0 <= new_row < ROWS and 0 <= new_col < COLS
                    
                    if is_valid:
                        is_land = grid[new_row][new_col] == 0
                        is_new = not (new_row, new_col) in visited

                        if is_land and is_new:
                            que.append((new_row, new_col))
                            visited.add((new_row, new_col))
            return is_closed

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        closed_islands = 0
    
        for row in range(ROWS):
            for col in range(COLS):
                is_land = grid[row][col] == 0
                is_new = not (row, col) in visited

                if is_land and is_new and is_closed_island(row, col):
                    closed_islands += 1

        return closed_islands