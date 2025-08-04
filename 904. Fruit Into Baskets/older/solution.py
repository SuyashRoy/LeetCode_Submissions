from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # if len(fruits) == 0:
        #     max_count = 0
        # else:
        #     max_count = 1
        #     basket_one_type = fruits[0]
        #     last_window_index = 0
        #     start_window_index = 0
        # i = 1
        # basket_two_type = -1
        # while(i < len(fruits)):
        #     if fruits[i] != basket_one_type and basket_two_type == -1:
        #         basket_two_type = fruits[i]
        #         last_window_index = i
        #     elif fruits[i] == basket_one_type or fruits[i] == basket_two_type:
        #         last_window_index = i
        #     elif fruits[i] != basket_one_type and fruits[i] != basket_two_type:
        #         start_window_index = last_window_index
        #         last_window_index = i
        #         basket_one_type = basket_two_type
        #         basket_two_type = fruits[i]
        #     total_count = (last_window_index - start_window_index) + 1
        #     max_count = max(max_count, total_count)
        #     i+=1
        # return max_count

        ### Initializing variables
        max_count = 0
        start_index = 0
        bag_one_type = -1
        bag_two_type = -1
        last_basket = -1
        last_basket_index = -1
        i = 1

        if len(fruits) == 0:
            return 0
        else:
            bag_one_type = fruits[0]
        
        while(i < len(fruits)):
            if fruits[i] != bag_one_type and bag_two_type == -1:
                bag_two_type = fruits[i]
            
            elif fruits[i] != bag_one_type and fruits[i] != bag_two_type:
                start_index = last_basket_index
                if last_basket == bag_one_type:
                    bag_two_type = fruits[i]
                elif last_basket == bag_two_type:
                    bag_one_type = fruits[i]
                last_basket = fruits[i]
                last_basket_index = i
            if fruits[i] == bag_one_type or fruits[i] == bag_two_type:
                if fruits[i] == bag_one_type:
                    last_basket = bag_one_type
                    last_basket_index = i
                elif fruits[i] == bag_two_type:
                    last_basket = bag_two_type
                    last_basket_index = i
            total_count = (i - start_index) + 1
            max_count = max(max_count, total_count)
            i += 1
                
            


        
        
            
