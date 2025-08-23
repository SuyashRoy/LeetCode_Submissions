class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ""
        palindrome = ""
        temp = ""
        if len(s) == 1:
            return s
        if len(s) == 0:
            return ""
        for i in range(len(s)):
            substring += s[i]
            temp+=s[i]
            for j in range(i+1, len(s)):
                substring+=s[j]
                if substring[::-1] == substring:
                    temp = substring
            if len(temp) > len(palindrome):
                palindrome = temp  
            substring = ""
            temp = ""    
        return palindrome

### Example usage:
solution = Solution()
print(solution.longestPalindrome("babad"))  ### Output: "bab" or "aba"
print(solution.longestPalindrome("cbbd"))   ### Output: "bb"
print(solution.longestPalindrome("a"))      ### Output: "a"