class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # Declarar variáveis:
        even_counts = {}
        highest_frequency = -1
        most_frequent_even = -1

        # Contar a frequência dos números pares (armazenamento em tuplas - número e contagem do mesmo):
        for num in nums:
            if num % 2 == 0:
                if num in even_counts:
                    even_counts[num] += 1 
                else: 
                    even_counts[num] = 1

        # Encontrar o número par mais frequent (iterar sobre cada tupla de even_counts - número e contagem do mesmo):
        for num, count in even_counts.items():
            if count > highest_frequency or (count == highest_frequency and num < most_frequent_even):
                most_frequent_even =  num
                highest_frequency = count
        
        return most_frequent_even


        


        

        