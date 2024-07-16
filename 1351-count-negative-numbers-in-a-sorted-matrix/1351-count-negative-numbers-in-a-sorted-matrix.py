class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative_numbers = []
        
        for row in grid:
            for element in row:
                if element < 0:
                    negative_numbers.append(element)
                    
        return len(negative_numbers)
        
        
        