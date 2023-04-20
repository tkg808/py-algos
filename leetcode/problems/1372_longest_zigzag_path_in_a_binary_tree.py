'''
========================================
1372. Longest ZigZag Path in a Binary Tree
========================================
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:
- Choose any node in the binary tree and a direction (right or left).
- If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
- Change the direction from right to left or from left to right.
- Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0

Constraints:
The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100

========================================
Breadth-First Search
- You can use DFS for this problem, and the implementation would be very similar, but I found that BFS is more intuitive in solving this problem for me personally
- Essentially, for each node, we will keep track of the previous direction traveled from the node's parent and the length of the path coming from the parent
- To continue on that path, we flip the direction and increment the length
- To account for the longest path potentially starting at a non-root node of the tree, we also search toward the same direction and reset the length for each node

Algo
- Use an integer variable to keep track of the max zigzag length -> max_length
- Use a que to implement an iterative BFS starting at the root node of the tree -> que
- Loop until que is empty
    -- Get first in que -> node, direction, path_length
    -- Try to update max_length
    -- Check left child
        --- Continue/start path toward left child depending on the previous direction
    -- Check right child
        --- Continue/start path toward right child depending on the previous direction
- After all paths have been searched -> Return max_length

Performance
- Let n be the number of nodes in the tree
- Time
    -- Searching all nodes in the tree costs O(n)
    -- Overall -> O(n)
- Space
    -- Using a que to implement the BFS costs O(n)
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ''' ===== BFS - Iterative ===== '''
        max_length = 0
        que = deque([])

        if root.left:
            que.append((root.left, True, 1))
        if root.right:
            que.append((root.right, False, 1))

        while que:
            node, from_left, path_length = que.popleft()

            max_length = max(max_length, path_length)

            if node.left:
                new_length = path_length+1 if not from_left else 1
                que.append((node.left, True, new_length))
            if node.right:
                new_length = path_length+1 if from_left else 1
                que.append((node.right, False, new_length))

        return max_length