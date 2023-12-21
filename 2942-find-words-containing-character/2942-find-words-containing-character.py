class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        # Criar uma lista vazia para armezanar os índices
        result = []

        # Iterar o array
        for i in range(0, len(words)):
            if x in words[i]:
                result.append(i)

        # Retornar resultado
        return result
        