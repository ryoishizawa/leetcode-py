"""
## Result
Runtime: 32 ms, faster than 97.02% of Python3 online submissions for Valid Anagram.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Valid Anagram.

## Complexity:
- Time complexity: O(n)
- Space complexity: O(1)

Ref: https://github.com/twtrubiks/leetcode-python/blob/master/242%20Valid%20Anagram.py
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_array = [0] * 123
        for i in t:
            count_array[ord(i)] += 1
        for i in s:
            count_array[ord(i)] -= 1
        for i in count_array:
            if i != 0:
                return False
        return True
