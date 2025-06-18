'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=0
        result=""
        for x in range(len(s)):
            for j in range(x,len(s)):
                substr = s[x:j+1]
                if substr ==substr[::-1]and len(substr)>length:
                    result = substr
                    length = len(substr)
        return result       
Sol = Solution()
test_case_1 = "babad"
test_case_2 = "cbbd"
result = Sol.longestPalindrome(test_case_1)
print(result)  