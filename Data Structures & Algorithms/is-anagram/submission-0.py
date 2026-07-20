class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check the length
        if len(s) != len(t):
            return False
        #make a hashmap with s populated
        hmap = {}
        for i in s:
            hmap[i] = hmap.get(i,0) + 1
        #subtract 1 for each letter from t hashmap 
        for j in t:
            if j not in hmap or hmap[j] == 0:
                return False
            hmap[j] = hmap.get(j,0) - 1 
        return True      