class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Função que verifica se todas as letras de uma palavra estão na mesma linha do teclado
        def is_in_same_row(word):
            # Linhas do teclado
            rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

            # Obtém o primeiro caractere da palavra em minúsculas
            first_char = word[0].lower()

            # Verifica em qual linha do teclado está o primeiro caractere
            for row in rows:
                if first_char in row:
                    # Verifica se todas as letras da palavra estão na mesma linha
                    return all(char.lower() in row for char in word)

            # Se o primeiro caractere não foi encontrado em nenhuma linha, retorna False
            return False

        # Lista de palavras que estão na mesma linha do teclado
        result = [word for word in words if is_in_same_row(word)]

        # Retorna a lista resultante
        return result
