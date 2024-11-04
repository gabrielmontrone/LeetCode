class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        answer = []
    
        for j in nums[0]:
            found_in_all = True

            for i in range(1, len(nums)):
                if j not in nums[i]:
                    found_in_all = False
                    break
            
            if found_in_all and j not in answer:
                answer.append(j)
        
        return sorted(answer)

        