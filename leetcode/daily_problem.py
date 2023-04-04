'''
========================================
2405. Optimal Partition of String
========================================
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

Constraints:
1 <= s.length <= 105
s consists of only English lowercase letters.

Example 1:
Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.

Example 2:
Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").

========================================
Initial Thoughts
- This problem asks us to find substrings of s that have no duplicate characters
- We can build substrings by keeping track of the starting index of a substring and then searching for a duplicate to indicate the end of the current substring and the start of the next substring
- We can determine that a character is a duplicate if the same character has already been seen after the starting index
- This essentially describes a sliding window solution that greedily adds non-duplicates to a substring and relies on a hashmap to determine if a character is a duplicate or not

Algo
- Use an integer to keep track of the total number of substrings -> substrings_count
- Use a hashmap to keep track of the last index a character was seen at -> last_index
- Use an integer to keep track of the starting index of the current substring -> substring_start
- Iterate s -> i, char
    - If char is a dupe -> Increment substrings_count -> Update substring_start
    - Update last_index for char
- Since substrings_count is updated when a new substring is created, we have to account for the substring at the end of s -> so we return substrings_count + 1

Performance
- Let n be the length of s
Time
  - Iterating each character of s costs O(n)
  - The operations on our hashmap costs O(1)
  - Converting a character to it's ASCII code costs O(1)
  - Overall -> O(n)
Space
    - Since this problem only uses lowercase English letters, the cost of last_index hashmap is constant
    - Overall -> O(1)

========================================
'''

class Solution:
    def partitionString(self, s: str) -> int:
        ''' ===== Sliding Window ===== '''
        
        def get_index(char: str):
            return ord(char) - ord('a')

        substrings = 0
        last_index = [-1 for _ in range(26)]
        substring_start = 0

        for i, char in enumerate(s):
            char_index = get_index(char)
            is_dupe = last_index[char_index] >= substring_start

            if is_dupe:
                substrings += 1
                substring_start = i

            last_index[char_index] = i

        return substrings + 1