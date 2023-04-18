'''
========================================
1768. Merge Strings Alternately
========================================
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 
Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

========================================
Initial Thoughts
- We could take characters from word2 and insert them into word1 at the appropriate indices...but modifying a string costs O(n), so it wouldn't be efficient

========================================
Two Pointers
- The intuition here is to use pointers to traverse each input string individually and add the characters to the merged string at each step
- Since strings are immutable in Python, we can use an array to keep track of the characters until the end where we can join them to efficiently create the output

Algo
- Use an array to store the characters of the merged string -> builder
- Use two pointers to traverse the input strings -> pos1, pos2
- Loop until both pointers reach the end of their respective word
    - If pos1 is not at the end -> Add char at pos1 to builder
    - If pos2 is not at the end -> Add char at pos2 to builder
- Join the characters in builder -> Return

Performance
- Let m be the length of word1
- Let n be the length of word2
- Time
    -- Using pointer variables costs O(1)
    -- Traversing the input strings costs O(max(m, n))
    -- Joining the builder array costs O(m + n)
    -- Overall -> O(m + n)
- Space
    -- Typically the space used for the output does not count toward the space complexity, but we are not returning an array for this problem, therefore the space for the builder array should be considered...and the cost is O(m + n)
    -- Overall -> O(m + n)

========================================
One Pointer
- This approach doesn't provide an improvement to time or space, but it can be considered cleaner and worth knowing
- Rather than using a pointer to traverse each input string, we can modify the Two Pointers approach to use a single pointer and take advantage of the checks already in-place for adding characters

Algo
- Use an array to store the characters of the merged string -> builder
- Use a for loop to iterate from 0 to the end of the longest input string -> pos
    - If pos is not at the end of word1 -> Add word1[pos] to builder
    - If pos is not at the end of word2 -> Add word2[pos] to builder
- Join the characters in builder -> Return

Performance
- As mentioned before, the time and space does not change from the Two Pointers approach
    -- Time -> O(m + n)
    -- Space -> O(m + n)

========================================
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ''' ===== Two Pointers ===== '''
        # builder = []
        # pos1 = 0
        # pos2 = 0
        
        # while pos1 < len(word1) or pos2 < len(word2):
        #     if pos1 < len(word1):
        #         builder.append(word1[pos1])
        #         pos1 += 1

        #     if pos2 < len(word2):
        #         builder.append(word2[pos2])
        #         pos2 += 1

        # return ''.join(builder)

        ''' ===== One Pointer ===== '''
        builder = []
        end = max(len(word1), len(word2))

        for pos in range(end):
            if pos < len(word1):
                builder.append(word1[pos])

            if pos < len(word2):
                builder.append(word2[pos])

        return ''.join(builder)