public class Solution {
    public int[] TwoSum(int[] nums, int target) {

        // Criar um dicionário para armezenar os números já "vistos"
        Dictionary<int, int> numIndexMap = new Dictionary<int, int>();

        // Iterar pela matriz "nums", calculando o complemento necessário 
        // para atingir o alvo
        for (int i = 0; i < nums.Length; i++) {
           int complement = target - nums[i];
        
            // Verifica se o complemento já está no dicionário
            if (numIndexMap.ContainsKey(complement)) {
                // Retorna o índice dos números que somam o alvo
                return new int[] { numIndexMap[complement], i};   
            }

            // Adiciona o número atual e seu índice ao dicionário
            numIndexMap[nums[i]] = i;
        }

        // Caso não encontre uma solução
        return new int[0];      
}
}