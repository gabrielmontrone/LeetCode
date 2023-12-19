class Solution:
    def divideArray(self, nums: List[int]) -> bool:
            
         # Verificar se o número de elementos é par
        if len(nums) % 2 != 0:
            return False

        # Ordenar a lista
        nums.sort()

        # Iterar sobre a lista e verificar se os elementos adjacentes são iguais
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i+1]:
                return False

        # Se todos os pares adjacentes são iguais, retorna True
        return True

        