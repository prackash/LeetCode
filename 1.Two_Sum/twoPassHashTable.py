from typing import List
class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            hashTable[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashTable and hashTable[complement] != i:
                return [i,hashTable[complement]]
        return None
    

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums,target))