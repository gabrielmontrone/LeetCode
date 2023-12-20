class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        # Inicializar lista de resultados
        result = []

        # Metódo para definir se é "self dividing number"
        def is_DividingNumber(s: int):
            numero_string = str(s)

            for indice in range(len(numero_string)):
                digito = int(numero_string[indice])

                if digito == 0 or s % digito != 0:
                    return False

            return True

        # Looping no range especificado
        for i in range(left, right + 1):
            if is_DividingNumber(i): 
                result.append(i)
        
        # Retorna o resultado
        return result
        
        