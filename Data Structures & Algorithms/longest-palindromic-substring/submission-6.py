class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0   

        #edge case: 1 character
        if not s:
            return ""

        for i in range(len(s)):
            #odd length
            #set l,r pointers: l goes left, r goes right from middle
            l,r = i,i
            while l >= 0 and r <len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1   

                #increment l & r
                l -= 1
                r += 1
            
            #even length
            #set l,r pointers: l goes left, r goes right from middle
            l,r = i,i+1
            while l >= 0 and r <len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1   

                #increment l & r
                l -= 1
                r += 1
        return s[resIdx : resIdx + resLen]





        