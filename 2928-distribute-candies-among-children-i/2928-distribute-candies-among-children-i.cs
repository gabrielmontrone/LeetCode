public class Solution {
    public int DistributeCandies(int n, int limit) {

        // Variável para contar quantas maneiras possíveis podemos distribuir os doces
        int contador = 0;


        // Lógica para distribuição
        for (int a = 0; a <= limit; a++) {
            for (int b = 0; b <= limit; b++) {
                for (int c = 0; c <= limit; c++) {
                    if (a + b + c == n && a <= limit && b <= limit && c <= limit) {
                        contador++;
                    }
                }
            }
        }

        return contador;
    }
}
