class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Inicializar os dicionários
        ransom_count = {}
        magazine_count = {}
        
        # Contar frequência dos caracteres
        for char in ransomNote:
            if char in ransom_count:
                ransom_count[char] += 1
            else:
                ransom_count[char] = 1
                
        for char in magazine:
            if char in magazine_count:
                magazine_count[char] += 1
            else:
                magazine_count[char] = 1
                
        # Comparar caracteres dos dicionários
        for char in ransom_count:
            if char not in magazine_count or ransom_count[char] > magazine_count[char]:
                return False
        return True
        