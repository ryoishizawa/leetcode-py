'''
Use recursion.

Time Complexity: O(n^2)

Can be improved:
- Add Exeption if there's no match
- Use Hash table to decrease time complexity
'''
class Solution:
    def __init__(self):
        self._firstIndex = 0
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        secondIndex = self._firstIndex
        for i in nums[1:]:
            secondIndex = secondIndex + 1
            if nums[0] + i == target:
                return [self._firstIndex, secondIndex]
        self._firstIndex = self._firstIndex + 1
        return Solution.twoSum(self, nums[1:], target)
