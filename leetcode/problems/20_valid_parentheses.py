'''
========================================
20. Valid Parentheses
========================================
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
Explanation: fails the first rule

Example 4:
Input: s = "([)]"
Output: false
Explanation: fails the second rule

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

========================================
Notes
- I will be referring to opening brackets as openers and closing brackets as closers
- Consider the rules for valid input string, we observe invalid cases
    -- s = ([] -> there is an unpaired opener (rule 1)
    -- s = (] -> opener does not have closer of the same type (rule 1)
    -- s = ([)] -> openers are not closed in the correct order (rule 2)
    -- s = ()] -> rule 3 -> there is an unpaired closer (rule 3)

========================================
Naive Approach
- A naive solution may include using one loop to choose an opener and then using a nested loop to find a valid/matching closer
- Using a nested loop would cost O(n**2), so we would want to explore other options that may be better 

========================================
Stack
- The important thing to understand for this problem is how to handle nested pairs
- Essentially, when we encounter a closer, it must be paired with the most recent unpaired opener
- This detail is a clue to use a stack, since stacks will allow us keep track of all openers in an order that lets us easily get the most recently seen opener
- Now, in order to validate if an opener and a closer are of the same type, we can take advantage of their place in the ASCII table
    -- '(' and ')' are next to each other in the table, so we can say they have a distance of 1
    -- There is a char between '[' and ']', so we would have to say they have a distance of 2
    -- There is a char between '{' and '}', so we would have to say they have a distance of 2
    -- Since s will only contain these six characters, we only need to confirm the distance between an opener and closer is either 1 or 2 on the ASCII table to validate the pair

Algo
- Use a stack to keep track of the unpaired openers -> stack
- Iterate s -> char
    - If char is an opener -> Add to stack
    - If char is a closer ->
        - Get top element from stack -> opener
        - If there is no opener for this closer -> Return False
        - If top of stack is a different type than closer -> Return False
        - Otherwise -> Pair opener with closer -> Continue
- If there are any unpaired openers -> Return False
- Otherwise -> Return True

Performance
- Let n be the length of s
Time ->
    -- Iterating s costs O(n)
    -- Adding/removing top of stack costs O(1)
    -- Overall -> O(n)
Space ->
    -- Using a stack can cost up to O(n)
    -- Overall -> O(n)

========================================
'''

class Solution:
    def isValid(self, s: str) -> bool:
        ''' ===== Stack ===== '''
        def is_valid_pair(opener, closer):
            ascii_distance = ord(closer) - ord(opener)
            return ascii_distance == 1 or ascii_distance == 2

        def is_opener(char):
            return char == '(' or char == '[' or char == '{'

        stack = []

        for char in s:
            if is_opener(char):
                stack.append(char)
            else:
                if not stack or not is_valid_pair(stack[-1], char):
                    return False
                
                stack.pop()

        return True if not stack else False