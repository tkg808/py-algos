'''
========================================
662. Maximum Width of Binary Tree
========================================
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:
Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).

Constraints:
The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100

========================================
Naive BFS *** TLE ***
- The problem involves interacting with each level of the tree, so using a level-order traversal (BFS) to get each level makes the most sense to me
- We can use a 2D array to store the nodes at each level, then iterate the 2D array to calculate the width of each level
- We can use a global variable to keep track of the max width while iterating the 2D array
- The problem now is making sure each node is in the correct index of their levels[i] array
    -- Consider level i of some tree -> levels[i] = 1, 2, N, 4
    -- Now consider the next level -> levels[i+1] = 11, 12, 21, 22, N, N, 41, 42
    -- So in order to correctly calculate the width of levels[i+1], we can store null nodes in the 2D array and 

Performance
- Let n be the number of nodes in the tree
- Time
    -- BFS costs O(n)
    -- Calculating the width for each level costs O(n)
    -- Overall -> O(n + n) -> O(n)
- Space
    -- The 2D array costs O(n)
    -- Overall -> O(n)

========================================
BFS - Optimized
- Despite the time complexity being linear, a large enough input will be a problem for the naive solution due to having a high constant
- Using BFS was the correct intuition, but we can optimize the way the width is calculated
    -- Firstly, rather than storing all null and non-null nodes, we can keep track of the column index for each node
        --- This is basically the reverse of the parent index calculation from the naive approach
        --- Here we'll use a node's column index to calculate it's child's column index
        --- This will account for null nodes that come before a node without having to store them
    -- Secondly, rather than essentially traversing the tree again to calculate the width of each level, we can calculate the width once all nodes in a level are accounted for
        --- Since each node will be accompanied by it's column index, we just need to take the first and last node of each level and use their column indices to calculate the width of the level -> last - first + 1

Algo
- Use an integer variable to keep track of the max width for all levels -> max_width
- Use a que to implement an iterative BFS -> que
- Initialize que with the root
- Loop until que is empty
    -- At the start of the loop, que holds all nodes for the current level -> calculate width for the current level
    -- Loop through the nodes of the current level to prepare the next level
- After all levels are accounted for -> Return max_width

Performance
- Let n be the number of nodes in the tree
- Time
    -- BFS costs O(n)
    -- Calculating the width for each level costs O(1)
    -- Overall -> O(n)
- Space
    -- The truth is our que will hold at most 2 levels worth of nodes at a time, but for simplicity's sake we can say O(n)
    -- Overall -> O(n)

========================================
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ''' ===== BFS - Optimized ===== '''
        max_width = 0
        que = deque([(root, 0)])

        while que:
            first_index = que[0][1]
            last_index = que[-1][1]
            curr_width = last_index - first_index + 1
            max_width = max(max_width, curr_width)

            for _ in range(len(que)):
                node, col_index = que.popleft()

                if node.left:
                    que.append((node.left, 2*col_index))
                if node.right:
                    que.append((node.right, 2*col_index+1))

        return max_width