class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ### if ransomNote has more letters than magazine, it cannot be recreated
        if len(magazine) < len(ransomNote):
            return False
        
        ### Dictionary to store and check frequencies of letters
        magLetters = {}
        
        ### Count the frequency of each character in the magazine
        for l in magazine:
            magLetters[l] = magLetters.get(l, 0) + 1
        
        ### Check if we can construct ransomNote from magazine
        for c in ransomNote:
            letterCount = magLetters.get(c, 0)
            if letterCount == 0:
                return False
            else:
                magLetters[c] -= 1
        
        return True
    
### Example usage
solution = Solution()
print(solution.canConstruct("a", "b"))      ### Output: False
print(solution.canConstruct("aa", "ab"))    ### Output: False
print(solution.canConstruct("aa", "aab"))   ### Output: True