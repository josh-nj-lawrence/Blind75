class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # Merge list
        lst = nums1 + nums2
        # Resort
        lst = sorted(lst)
        # Return median
        if len(lst)%2 == 0:
            # Even
            return float(lst[int(len(lst)/2 - 1)] + lst[int(len(lst)/2)])/2
        else:
            # Odd
            return float(lst[int(len(lst)//2)])
        return lst


sol = Solution()
print(sol.findMedianSortedArrays([1,2],[3,4]))