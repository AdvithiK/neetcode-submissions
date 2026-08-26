class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hashmaps storing character:count
        hmaps = {}
        hmapt = {}

        #edge case if length is unequal
        if len(s) != len(t):
            return False
        
        #populate the hashmap with chars from s
        for i in range(len(s)):
            hmaps[s[i]] = 1 + hmaps.get(s[i],0)
            hmapt[t[i]] = 1 + hmapt.get(t[i],0)
        return hmaps == hmapt
                



