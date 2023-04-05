'''
========================================
2439. Minimize Maximum of Array
========================================
You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:
Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.

Return the minimum possible value of the maximum integer of nums after performing any number of operations.

Constraints:
n == nums.length
2 <= n <= 105
0 <= nums[i] <= 109

Example 1:
Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.

Example 2:
Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.

========================================
Notes
- The problem wants us to find the smallest possible max value of nums 
- But when you decrease the value at nums[i], you have to increase the value at nums[i-1]
- You can't use i = 0 to decrement nums[i] because there is no i-1 to increment
- Problem -> How do we determine which index should be decremented?
    -- We can see from example 1, we decrement nums[i] when nums[i] is larger than nums[i-1]

========================================
Naive Approach
- The most naive intuition would be to take the max value of nums -> max_val
- Then loop through nums to operate on all values equal to max_val
- If there were any operations done, we decrement max_val and repeat the process
- Once there are no operations done -> Return max_val

Performance
- Let n be the size of nums
- Let k be the max value of nums
Time ->
    - Iterating nums costs O(n)
    - The number of operations to reach the minimum max value is O(k)
    - Overall -> O(n * k)
Space ->
    - No extra space is needed
    - Overall -> O(1)

========================================
Binary Search + Prefix Sums
- As unintuitive as this may seem, it is actually an important step toward the optimal solution
- The problem with the naive approach is that we eliminate candidates for max_val one at a time when we decrement a candidate
- Instead, we can use binary search to pick a candidate max_val, test if the candidate max_val is possible, and then logarithmically reach the minimum max_val
- How do we determine if a candidate max_val is possible/valid? Consider the following...
    -- Assume we have an array -> a b c d
    -- If we balance a and b -> a+1 b-1 c d
    -- Now if we balance b c -> a+1 b-1+1 c-1 d
    -- Which is the same as -> a+1 b c-1 d
    -- Therefore, we can decrement any index j in nums where j > 0 and increment any/all indices i in nums where i < j
    -- In other words, the decremented amount at some index j can be distributed among all indices less than j as long as each index does not exceed the candidate max_val
    -- This can be written as -> sum([nums[0], ..., nums[j-1]]) <= candidate * (j+1)
    -- Rather than calculating the sum of a subarray everytime we test a candidate, we can use an array to store the prefix sum for each index, which is the sum of all values up to (but not including) the index  -> prefix_sums[j] <= candidate * (j+1)

Performance
- Let n be the size of nums
- Let k be the max value of nums
Time ->
    - Iterating nums costs O(n)
    - The number of calls to binary search for a max_val candidate is O(log(k))
    - Accessing the prefix sums array costs O(1)
    - Overall -> O(n * log(k))
Space ->
    - Using an array to store prefix sums costs O(n)
    - Overall -> O(n)

========================================
Prefix Sum + Greedy
- To get to this approach, we have to inspect the condition for testing a candidate max_val in the binary search approach -> prefix_sums[j] <= candidate * (j+1)
- We can manipulate the condition such that we know the exact minimum max_val that is possible at index j based on the prefix sum -> prefix_sums[j] / (j+1)) <= candidate
- Now we can find the answer in one-pass
- Since we only need the previous prefix sum for our calculations, we can also improve the space complexity by using an accumulating integer variable instead of an array to store prefix sums

Algo
- Use an integer to keep track of the minimum max value for output -> max_val
- Use an integer to store the prefix sum -> prefix_sum
- Loop through nums -> i
    - Update prefix_sum
    - Calculate the minimum possible value for the current index -> curr_min
    - Update max_val if possible
- After the loop -> Return max_val

Performance
- Let n be the size of nums
Time ->
    - Iterating nums costs O(n)
    - Overall -> O(n)
Space ->
    - No additional space is used
    - Overall -> O(1)

========================================
'''

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ''' ===== Prefix Sum + Greedy ===== '''
        max_val = 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            curr_min = ceil(prefix_sum / (i+1))
            
            max_val = max(max_val, curr_min)
        
        return max_val