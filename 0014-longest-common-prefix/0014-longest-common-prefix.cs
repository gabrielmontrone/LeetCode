public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        
        // Garantir que a string não esteja vazia
        if (strs.Length < 1 || strs.Contains(""))
        {
            return string.Empty;
        }

        // Achar a menor palavra da string para iterarmos até ela
        string smallestWord = strs[0];

        foreach (string word in strs) 
        {
            if (word.Length < smallestWord.Length)
            {
                smallestWord = word;
            }
        }

        // Iniciando a variável que "marca" o tamanho do prefixo
        int commonLength = 0;

        // Looping de iteração
        for (int i = 0; i < smallestWord.Length; i++) 
        {
            char currentChar = smallestWord[i];

            // Verificar se o caractere atual está presente em todas as palavras
            if (strs.All(word => word[i] == currentChar))
            {
                commonLength++;
            }
            else
            {
                break;
            }
        }

        // Mostrar o prefixo comum
        string commonPrefix = smallestWord.Substring(0, commonLength);
   
        return commonPrefix;
    }
}