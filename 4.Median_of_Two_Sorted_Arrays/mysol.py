from typing import List
class Solution:
    def findMedianSortedArrays(self,nums1:List[int],nums2:List[int])->float:
        finlist = sorted(nums1+nums2)
        return finlist[len(finlist)//2] if len(finlist)%2!=0 else (finlist[len(finlist)//2]+finlist[len(finlist)//2-1])/2


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,3],[2])) # 2.0