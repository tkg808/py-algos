'''
========================================
2348. Number of Zero-Filled Subarrays
========================================
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109

========================================
Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6

====================
Notes
valid_subarrays =
  nums[2:3] -> 0
  nums[2:4] -> 0 0
  nums[3:4] -> 0
  nums[5:6] -> 0
  nums[5:7] -> 0 0
  nums[6:7] -> 0

output = len(valid_subarrays) = 6

========================================
Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9

====================
Notes
valid_subarrays =
  nums[2:3] -> 0
  nums[2:4] -> 0 0
  nums[3:4] -> 0
  nums[5:6] -> 0
  nums[5:7] -> 0 0
  nums[6:7] -> 0

========================================
'''

'''
========================================
Solutions
========================================
Naive Approach
- Create every contiguous subarray of nums to find the number of zero-filled subarrays
- This approach would have a quadratic time complexity, so we try to find a better solution

Performance
- Let n be the length of nums
Time -> O(n**2)
Space -> O(n)

========================================
Sliding Window
- The problem with the naive approach is that we would essentially have a loop to iterate the starting index of a subarray and then a nested loop to find the ending index of a subarray
- The important thing to realize is that we are able to determine the number of zero-filled subarrays within an array of all zeros by using math, specifically combinatorics
- Let's consider the following
  - If we were given -> nums = 0 0 0
  - We can use combinatorics to calculate the number of ways to choose the starting and ending indices of each zero-filled subarray
    - start = 0 -> end = 1, 2, 3 -> 3 subarrays
    - start = 1 -> end = 2, 3 -> 2 subarrays
    - start = 2 -> end = 3 -> 1 subarray
  - Therefore, the total number of zero-filled subarrays would be -> 3 + 2 + 1 = 6
  - This is actually known as the sum of an arithmetic series -> n * (n + 1) // 2

Algorithm
- Use an integer to keep track of the output -> zero_filled_subarrays
- Use a pointer to keep track of the starting index of the current subarray -> left
- Use a pointer to keep track of the ending index of the current subarray -> right
  - When left points to a non-zero element -> Left moves to right
  - When right points to a non-zero element -> Calculate the number of subarrays -> Update zero_filled_subarrays
- Once left reaches the end of nums -> Return zero_filled_subarrays

Performance
- Let n be the length of nums
Time -> O(n)
Space -> O(1)

========================================
Counting Zeros
- This is a similar approach to the Sliding Window approach, but it may be more intuitive
- Rather than managing pointers to get the size of the sliding window, we can just use an integer to keep count of currently consecutive zeros
- Then when a non-zero is found, the Sum of an Arithmetic Series formula can be

Algorithm
- Use an integer to keep track of the output -> zero_filled_subarrays
- Use an integer to keep track of the number of consecutive zeros recently seen -> curr_zeros
- Iterate nums -> num
  - If num is a zero -> Increment curr_zeros
  - If num is not a zero
    - Calculate valid subarrays using curr_zeros -> Update zero_filled_subarrays
    - Reset curr_zeros to 0
- After the loop, check if curr_zeros indicates that there was a valid subarray at the end of nums
- Return zero_filled_subarrays

Performance
- Let n be the length of nums
Time -> O(n)
Space -> O(1)

========================================
'''

from typing import List

class Solution:
  def zero_filled_subarray(self, nums: List[int]) -> int:
    ''' ===== Sliding Window ====='''
    # zero_filled_subarrays = 0
    # left = 0

    # for right in range(len(nums)):
    #   if nums[right] == 0 and nums[left] != 0:
    #     # Start of a new valid subarray
    #     left = right

    #   if nums[right] != 0:
    #     if nums[left] == 0:
    #       # End of the current valid subarray
    #       size = right - left
    #       zero_filled_subarrays += size * (size+1) // 2
    #     # left should be moved to the index just after right, which will allow us to determine if there is a subarray that needs to be calculated for after the loop terminates
    #     left = right + 1

    # # Check if there is a subarray at the end of nums that needs to be calculated for
    # if left < len(nums):
    #   size = len(nums) - left
    #   zero_filled_subarrays += size * (size+1) // 2
        
    # return zero_filled_subarrays

    ''' ===== Counting Zeros ====='''
    zero_filled_subarrays = 0
    # Keep track of the number of the current consecutive zeros seen
    curr_zeros = 0

    for num in nums:
      if num == 0:
        # Extend zero-filled subarray
        curr_zeros += 1
      else:
        # End of zero-filled subarray
        zero_filled_subarrays += curr_zeros * (curr_zeros+1) // 2
        # Reset consecutive zeros
        curr_zeros = 0

    # Check if there is a subarray at the end of nums that needs to be calculated for
    if curr_zeros:
      zero_filled_subarrays += curr_zeros * (curr_zeros+1) // 2

    return zero_filled_subarrays