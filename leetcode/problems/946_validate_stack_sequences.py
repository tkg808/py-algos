'''
========================================
946. Validate Stack Sequences
========================================
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2. 

Constraints:
1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.

========================================
Initial Thoughts
- My first instinct after seeing two correlating arrays was to use pointers to traverse each input array while accounting for push and pop operations
    -- This is mostly hopeful thinking, since using pointers would lower the cost for space
    -- However, only using pointers would not allow us to execute correct pop operations on the sequence
    -- Therefore, this approach would not be effective for this problem

========================================
Stack
- Although my first instinct was not correct, it did make me aware of two key requirements for this problem:
    --1 I will have to keep track of the values in a sequential order
    --2 I will have to maintain the order by adding/removing values to/from the end
- From this insight, I realize that a stack is an ideal choice
- Essentially, I can reproduce the sequence with a stack, and check for any invalidating cases throughout
- This approach looks at the problem in two phases
    -- The first phase -> Accounts for all push and pop operations until all pop values have been accounted for
    -- The second phase -> Accounts for the remaining values in the stack and remaining pop values 

Algo
- Use a helper function to the first phase
    -- Use a stack to keep track of the sequence -> stack
    -- Use a pointer to keep track of the current index in popped -> curr_pop
    -- Iterate pushed -> push_val
        --- Check if push_val matches the value at curr_pop
            ---- Skip the formalities of pushing then popping -> Increment curr_pop -> Continue
        --- If not, loop to check for consecutive pop operations
            ---- Pop from stack -> Increment curr_pop
        --- Once the pop loop is finished -> Add push_val to stack
    -- Return the state of the stack and curr_pop to be used for the next phase
- Use a helper function
- If curr_push has reached the end and we can't pop any more values from popped -> Return False
- Otherwise -> Return True

Performance
- Let n be the length of pushed/popped
Time ->
    -- Iterating the input arrays costs O(n)
    -- Operations on a stack costs O(1)
    -- Overall -> O(n)
Space ->
    -- Using a stack to verify the sequence costs O(n)
    -- Overall -> O(n)

========================================
Stack - Clean
- Although the previous approach is correct and optimal in terms of time/space, one could argue that it is an indirect solution
- The reason it is indirect stems from the decision to check if push_val matches the value at curr_pop
    -- In doing so, push_val gets added to the stack after we handle consecutive pop operations
    -- Which means that after the last push_val is added to the stack, the sequence is not accurate, which prompts a second phase of validating the remaining pop operations
- The key detail that I missed was that push_val should always be added to the stack before handling pop operations
- To make sense of this, consider the following
    -- Since there is nothing to pop from an empty stack, we'll say an empty stack is a valid sequence
    -- Adding push_val to a valid sequence potentially invalidates the sequence
    -- We use pop operations to re-validate the sequence
    -- Then we move onto the next push_val
    -- Therefore, we can be confident that at the beginning of each iteration, we have a valid sequence and that push_val should be added first

========================================
'''

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ''' ===== Stack ===== '''
        # def traverse_pushed():
        #     stack = []
        #     curr_pop = 0
            
        #     for push_val in pushed:
        #         if push_val == popped[curr_pop]:
        #             curr_pop += 1
        #             continue

        #         while stack and stack[-1] == popped[curr_pop]:
        #             stack.pop()
        #             curr_pop += 1
                
        #         stack.append(push_val)
        #     return (stack, curr_pop)

        # def handle_leftovers(sequence, pop_index):
        #     while sequence and pop_index < len(popped):
        #         if stack.pop() != popped[pop_index]:
        #             return False

        #         pop_index += 1

        #     return pop_index == len(popped) and not stack

        # stack, index = traverse_pushed()
        # is_valid_sequence = handle_leftovers(stack, index)

        # return is_valid_sequence

        ''' ===== Stack - Clean ===== '''
        stack = []
        curr_pop = 0
        
        for push_val in pushed:
            stack.append(push_val)

            while stack and stack[-1] == popped[curr_pop]:
                stack.pop()
                curr_pop += 1

        return curr_pop == len(popped)