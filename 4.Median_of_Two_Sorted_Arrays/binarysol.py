class Solution:
    def findMedianSortedArrays(self,nums1,nums2)->float:
        n1=len(nums1);
        n2 = len(nums2);
        if n1>n2:
            nums1,nums2 = nums2,nums1
        n = n1 +n2
        left = (n+1)//2
        low,high = 0,n1

        while low<=high:
            mid1 = (high+low)//2
            mid2 = left-mid1

            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')

            if mid1<n1:
                r1=nums1[mid1]
            if mid2<n2:
                r2=nums2[mid2]
            if mid1-1>=0:
                l1=nums1[mid1-1]
            if mid2-1>=0:
                l2=nums2[mid2-1]
            
            if l1<=r2 and l2<=r1:
                if n%2 == 1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2) + min(r1,r2))/2
            elif l1>r2:
                high = mid1-1
            else:
                low = mid1+1
        return 0

if __name__== "__main__":
    s= Solution()
    print(s.findMedianSortedArrays([1,2],[3,4,5])) # 2.0