class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rep_count = 0

        #sliding window where L s at the front & move R till repeat appears

        #set to store the resulting set & var to store size
        res_set = set()
        res_size = 0
        
        #set the L pointer, r pointer in the loop
        l = 0

        #loop through till r reachs end of s
        for r in range(len(s)):
            #remove everything up to r and move l if r is in the set (resetting l)
            while s[r] in res_set:
                res_set.remove(s[l])
                l += 1
            #otherwise add s[r] to set
            res_set.add(s[r])
            #set res to the max length found 
            res_size = max(res_size, r-l+1)
        return res_size


