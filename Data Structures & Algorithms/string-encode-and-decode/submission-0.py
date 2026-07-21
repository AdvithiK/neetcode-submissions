class Solution:
    #to encode, charnum = size of the word + delimiter = "#" + word
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            charnum = len(s)
            res+= str(charnum) + "#" + s
        #return the encoded string
        return res
    #to decode, take the string and seperate it into a list of strings
    def decode(self, s: str) -> List[str]:
        
        res = []
        #pointer to track where we are in the string
        i = 0

        #read each character
        while i < len(s):
            #find the delimiter with the second delimiter
            j = i
            while s[j] != "#":
                j+=1
            #find the charnum, j gives the length of the string
            charnum = int(s[i:j])
            #append word to res
            #j+1 is the char after #, and j+1+charnum is one after the end of the word
            res.append(s[j+1:j+1+charnum])

            #update i to j+1+charnum is one after the end of the word
            i = j+1+charnum
        
        return res


