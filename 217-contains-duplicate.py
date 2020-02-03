'''
Time Complexity: O(nlogN)
- Sort O(nlogN)
- Sweep O(n)

Better choice: Use Hash Table
Not to use: Brute force (Not Accepted as the time complexity is O(n^2))
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
