class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create two hashmaps for each word
        sMap = {}
        tMap = {}

        #edge case: lengths don't match, they aren't anagrams
        if len(s) != len(t):
            return False


        #populate both hashmaps
        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i],0) + 1
            tMap[t[i]] = tMap.get(t[i],0) + 1

        #return the equality of the two hashmaps
        return sMap == tMap