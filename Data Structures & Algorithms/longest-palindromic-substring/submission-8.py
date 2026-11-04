class Solution:
    def longestPalindrome(self, s: str) -> str:
        #store the res length & res starting index
        resLength = 0
        resStartIndex = 0 
        
        for i in range(len(s)):
            #odd length: start at the same index
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                #check if word length > resLength
                if (r-l+1) > resLength:
                    resStartIndex = l
                    resLength = r-l+1
                #increment l & r
                l -= 1
                r += 1

            #even length
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                #check if word length > resLength
                if (r-l+1) > resLength:
                    resStartIndex = l
                    resLength = r-l+1
                #increment l & r
                l -= 1
                r += 1
        return s[resStartIndex : resStartIndex + resLength]
        