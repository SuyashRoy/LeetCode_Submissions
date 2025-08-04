from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_count = 0
        start_index = 0
        bag_one_type = -1
        bag_two_type = -1
        last_basket = -1
        last_basket_index = -1
        i = 0

        while(i < len(fruits)):

            if(bag_one_type == -1):
                bag_one_type = fruits[i]
                
            elif(bag_two_type == -1 and fruits[i] != bag_one_type):
                bag_two_type = fruits[i]

            elif fruits[i] != bag_one_type and fruits[i] != bag_two_type:
                start_index = last_basket_index

                bag_one_type = bag_one_type if (last_basket == bag_one_type) else bag_two_type
                bag_two_type = fruits[i]
                last_basket = fruits[i]
                last_basket_index = i
            if(last_basket != fruits[i]):
                last_basket = fruits[i]
                last_basket_index = i
            total_count = (i - start_index) + 1
            max_count = max(max_count, total_count)
            i += 1

        return max_count
                
### Example usage:
fruits = [1, 2, 1]
fruits_2 = [0, 1, 2, 2]
fruits_3 = [1, 2, 3, 2, 2]
solution = Solution()
print(solution.totalFruit(fruits))  # Output: 3
print(solution.totalFruit(fruits_2))  # Output: 3
print(solution.totalFruit(fruits_3))  # Output: 4
                
            


        
        
            
