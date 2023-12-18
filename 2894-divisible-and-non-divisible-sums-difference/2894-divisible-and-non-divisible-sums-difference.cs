public class Solution {
    public int DifferenceOfSums(int n, int m) {
        
        // Variaveis para armazenar os valores divisiveis ou não
        int SomaDivisivel = 0;
        int SomaNaoDivisivel = 0;

        for (int i = 1; i <= n; i++) 
        {
            // Verificar se os números são divisíveis por "m"
            if (i % m == 0) 
            {
                SomaDivisivel += i;
            }

            else 
            {
                SomaNaoDivisivel += i;
            }
        }

        // Retornar a diferença das somas
        return SomaNaoDivisivel - SomaDivisivel;
    }
}