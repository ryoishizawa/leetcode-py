'''
version 2: Use Hash Table

Time Complexity: O(n)
    
Can be improved:
- Add exception if there's no match
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            hashTable[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashTable and hashTable.get(complement) != i:
                return [i, hashTable.get(complement)]
