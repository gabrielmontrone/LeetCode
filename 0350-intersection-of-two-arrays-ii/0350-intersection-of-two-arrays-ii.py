class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_intersect = []

        for i in nums1:
            if i in nums2:
                nums_intersect.append(i)
                nums2.remove(i)
    
        return nums_intersect

