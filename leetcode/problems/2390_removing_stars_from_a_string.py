'''
========================================
2390. Removing Stars From a String
========================================
You are given a string s, which contains stars *.

In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:
The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 
Example 1:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

Example 2:
Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.

========================================
Naive Approach
- You could probably use pointers to traverse s to find stars and remove the non-star to it's left directly, but operations directly on a string cost O(n) so the overall time would be quadratic
- Since our input can be up to 10**5 characters long, we should explore other solutions before settling with this one

Performance
- Let n be the length of s
Time ->
    -- Iterating s costs O(n)
    -- Modifying a string costs O(n)
    -- Overall -> O(n**2)
Space -> 
    -- Using pointers costs O(1)
    -- Overall -> O(1)

========================================
Stack
- An important detail for this problem is that we have to be able to access the most recently seen non-star characters in the order they were seen
    -- A stack is a perfect solution to this part of the problem
- Then upon finding a star character, we have to remove the most recently seen non-star character

Algo
- Use a stack to keep track of non-star characters in the order they appear in s -> stack
- Iterate s -> char
    - If char is not a star -> Add it to stack
    - If char is a star -> Remove the top element from stack
- After iterating s -> Join and return the stack

Performance
- Let n be the length of s
Time ->
    -- Iterating s costs O(n)
    -- Joining the stack costs O(n)
    -- Operations on our stack costs O(1)
    -- Overall -> O(n)
Space -> 
    -- Using a stack costs O(n)
    -- Overall -> O(n)

========================================
'''

class Solution:
    def removeStars(self, s: str) -> str:
        ''' ===== Stack ===== '''
        stack = []

        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()

        return ''.join(stack)