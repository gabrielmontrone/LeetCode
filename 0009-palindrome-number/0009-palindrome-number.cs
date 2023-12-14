public class Solution {
    public bool IsPalindrome(int x) {
       // Número negativo não é palíndromo 
       if (x < 0) {
           return false;
       }

       // Converter o número em uma string
       string numStr = x.ToString();

       // Iniciar dois ponteiros, um no início da string e outro no final
       int i = 0;
       int j = numStr.Length - 1;

       // Compara os caracteres
       while (i < j) {
           if (numStr[i] != numStr[j]) {
           return false;
           }

           i++;
           j--;
       }
       return true;
    } 
}