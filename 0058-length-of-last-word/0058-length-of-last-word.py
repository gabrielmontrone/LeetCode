class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Separar o input em palavras
        palavras = s.split()

        # Condição para saber se existe pelo menos uma palavra
        if palavras:
            return len(palavras[-1])

        # Retorne 0 caso não haja palavra
        else: 
            return False

        