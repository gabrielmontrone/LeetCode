public class Solution {
    public bool IsValid(string s) {
        Stack<char> stack = new Stack<char>();

        for (int i = 0; i < s.Length; i++) {
            char currentChar = s[i];

            if (currentChar == '(' || currentChar == '{' || currentChar == '[') {
                // Abre um parêntese, colchete ou chave, empilha na pilha
                stack.Push(currentChar);
            } else {
                // Fecha um parêntese, colchete ou chave, verifica se corresponde ao topo da pilha
                if (stack.Count == 0) {
                    return false; // Não há correspondência aberta
                }

                char topChar = stack.Pop(); // Obtém o topo da pilha

                // Verifica se a correspondência é válida
                if ((currentChar == ')' && topChar != '(') ||
                    (currentChar == '}' && topChar != '{') ||
                    (currentChar == ']' && topChar != '[')) {
                    return false; // Correspondência inválida
                }
            }
        }

        return stack.Count == 0; // Retorna true se todas as correspondências foram fechadas corretamente
    }
}