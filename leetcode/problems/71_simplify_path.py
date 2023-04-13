'''
========================================
71. Simplify Path
========================================
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:
The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
 
Constraints:
1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.

========================================
Initial Approach *** WRONG ***
- The problem is asking me to take the absolute path and convert it to it's canonical path
- Through inspecting the format of a canonical, I can see that it has an alternating pattern of ->  '/' + directory name
- So if I can parse the directory names from the input path, I can construct the canonical path for output
- Note that any character that is not a '.' or '/' is considered part of a directory name

Algo 
- Use an array to keep track of directory names -> directories
- Use a pointer to keep track of the starting index of a directory name -> start
- Iterate path to find directory names -> end
    -- Cases
        ---1 start is a dot or slash
            ---- Regardless of what end is, this can never form a valid directory name
        ---2 start is not a dot or slash AND end is a dot or slash
            ---- We have found the end of the directory name
        ---3 start is not a dot or slash AND end is not a dot or slash
            ---- We have a directory and we are looking for the ending index of it
    -- For case 1 -> Move start pointer to end pointer
    -- For case 2 -> Add the pointers to directories as a tuple -> Then move start pointer to end pointer
    -- For case 3 -> Continue searching for the ending index
- After path has been traversed, if there were no directories founnd -> Return '/'
- Otherwise, join directories by alterating '/' + directory name -> Return

Performance
- Let n be the length of path
- Let m be the max length of a directory
- Let k be the number of directories
Time ->
    -- Iterating path costs O(n)
    -- Storing pointers costs O(1)
    -- Creating each directory name string costs O(m * k)
    -- Overall -> O(n + m*k)
Space ->
    -- Storing pointers for each directory costs O(k)
    -- Creating each directory name string costs O(m * k)
    -- Overall -> O(m * k)

========================================
Stack
- The initial solution was incorrect because I misunderstood the problem
- Consider the following example:
    -- path = /a/b/../c/
    -- The initial approach would return -> /a/b/c
    -- But the correct output should be -> /a/c
- When initially trying to understand the problem, I didn't consider that this was the direction the problem was going
- From my experience importing files in ReactJS or NodeJS, something like '/a/c' would assume that there exists a directory/file 'c' in directory 'a'...so for '/a/b/../c/', something like '../../c' would be expected
- Regardless, I now realize that we can't simply ignore all dots
- Consider the following cases for dots:
    --1 Single dot -> /a/b/./c/
        --- Stay in parent/left directory -> Ignore the dot
        --- Output -> /a/b/c
    --2 Double dots -> /a/b/../c/
        --- Remove parent/left directory
        --- Output -> /a/c
    --3 All other forms of dots are treated as file/directory name
        --- More than two dots -> /a/b/.../c
        --- Dots not surrounded by slashes -> /a/b../c
- With this information, I now understand that the crux of the problem is accounting for case 2
- In order to handle case 2, I need to be able remove the correct parent directory when '/../' is encountered, even when the directory is not adjacent to the dots
- In order to know which parent directory is the correct one to remove, I need to keep track of the directories in the order they appear
- These are key indicators that a stack would be a good option for this problem

Algo
- Use a stack to keep track of the directories in the order they are seen -> stack
- Split the path by slashes and iterate -> section
    - If section is empty or a single dot -> Skip
    - If section is double dots -> Remove most recently seen parent directory if it exists
    - Otherwise -> Add section to stack
- After the loop -> Join directory names by alterating '/' + directory name -> Return

Performance
- Let n be the length of path
Time ->
    -- Splitting path costs O(n)
    -- Operations on a stack costs O(1)
    -- The sum of all individual directory names will never exceed n, so the cost to build the strings is no more than O(n)
    -- Overall -> O(n + n) -> O(n)
Space ->
    -- Using a stack to store the directory names can cost up to O(n)
    -- Overall -> O(n)

========================================
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        ''' ===== Stack ===== '''
        stack = []

        for section in path.split('/'):
            if not section or section == '.':
                continue

            if section == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(section)
            
        return '/' + '/'.join(stack)