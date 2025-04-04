from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res, int_max,diff_max =0,0,0
        for i in nums:
            res = max(res,diff_max*i)
            diff_max = max(diff_max,int_max-i)
            int_max = max(int_max,i)
        return res
if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution().maximumTripletValue(nums))
    nums = [1,5,3,2]
    print(Solution().maximumTripletValue(nums))
    nums = [3,2,1]
    print(Solution().maximumTripletValue(nums))
    nums = [1,2]
    print(Solution().maximumTripletValue(nums))
    nums = [1]
    print(Solution().maximumTripletValue(nums))