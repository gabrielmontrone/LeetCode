class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_diff = []
        nums2_diff = []

        for i in nums1:
            if i not in nums2 and i not in nums1_diff:
                nums1_diff.append(i)
        
        for i in nums2:
            if i not in nums1 and i not in nums2_diff:
                nums2_diff.append(i)

        return [nums1_diff, nums2_diff]
                
