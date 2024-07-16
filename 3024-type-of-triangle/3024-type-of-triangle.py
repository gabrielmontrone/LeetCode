class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Para um triângulo ser formado, a soma de dois lados deve ser maior que o terceiro lado
        a, b, c = nums
        equilateral = 'equilateral'
        isosceles = 'isosceles'
        scalene = 'scalene'
        none = 'none'
        
        if a + b > c and b + c > a and c + a > b:
            if a == b and b == c:
                return equilateral
            if (a == b and b != c) or (a == c and c != b) or (c == b and b != a):
                return isosceles
            if (a != b) and (b != c) and (c != a):
                return scalene
        else:
            return none
                
        