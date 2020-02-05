"""
Solved by @ryoishizawa

## Result (5th Feb 2019)
Runtime: 28 ms, faster than 72.47% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.

## Complexity
Time Complexity: O(n)
Space Complexity: O(1)

"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                ## Time complexity O(1)
                stack.append(ch)
            elif ch == ')' or ch == '}' or ch == ']':
                if len(stack) == 0:
                    return False
                ## Time complexity O(1)
                ch2 = stack.pop()
                if ch == ')':
                    if ch2 != '(':
                        return False
                elif ch == '}':
                    if ch2 != '{':
                        return False
                elif ch == ']':
                    if ch2 != '[':
                        return False
            else:
                ## Invalid word included
                return False
        if len(stack) == 0:
            return True
        return False
