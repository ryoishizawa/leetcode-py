"""
Solved by own, the result is not good.

Runtime: 976 ms, faster than 5.08% of Python3 online submissions for Valid Anagram.
Memory Usage: 13.7 MB, less than 28.13% of Python3 online submissions for Valid Anagram.

Time Complexity: O(n^2)
O(n) for creating list, O(n^2) for sweeping

Can be improved:
- If length doesn't match, you can return False immediately.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_list = []
        for i in t:
            anagram_list.append(i)
        for j in s:
            try:
                ## O(n) for index
                index = anagram_list.index(j)
            except ValueError:
                return False
            ## O(k) for pop
            anagram_list.pop(index)
        if len(anagram_list) == 0:
            return True
        return False
