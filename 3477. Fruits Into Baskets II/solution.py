from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        num_placed = 0
        placed = [-1] * len(fruits)
        basket_placed = [-1] * len(fruits)
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<= baskets[j] and placed[i] == -1 and basket_placed[j] == -1:
                    basket_placed[j] = i
                    placed[i] = j
                    num_placed+=1
        return (len(fruits) - num_placed)

### Example usage:
solution = Solution()
fruits_1 = [4, 2, 5]
fruits_2 = [3, 6, 1]
basket_1 = [3, 5, 4]
basket_2 = [6, 4, 7]

print(solution.numOfUnplacedFruits(fruits_1, basket_1))  ### Output: 1
print(solution.numOfUnplacedFruits(fruits_2, basket_2))  ### Output: 0
