class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        max_len = 0
        for index, string in enumerate(s):
            if string not in substring:
                substring += string
            else:
                max_len = max(max_len, len(substring))
                last_index = substring.index(string)
                substring+=string
                substring = substring[last_index+1:]  
        max_len = max(max_len, len(substring))
        return max_len

### Example usage:
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  ### Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     ### Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    ### Output: 3