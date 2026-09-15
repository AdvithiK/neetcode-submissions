class Solution:
    def countSubstrings(self, s: str) -> int:
        #have a L & R pointer at the center and check + expand
        res = 0
        
        for i in range(len(s)):
            #check for odd length
            left, right = i,i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            
            #check for even length
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

            
            


            

        