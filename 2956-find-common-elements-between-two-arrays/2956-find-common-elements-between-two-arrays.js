/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var findIntersectionValues = function(nums1, nums2) {
    
        // Criar os contadores
        let contador1 = 0;
        let contador2 = 0;

        // Iterar a lista 1 sobre a lista 2
        for (let n of nums1) {
            if (nums2.includes(n)) {
                contador1 += 1;
            }
        }

        // Iterar a lista 2 sobre a lista 1 
        for (let m of nums2) {
            if (nums1.includes(m)) {
                contador2 += 1;
            }
        }

        // Retornar contadores
        return [contador1, contador2];
    }
