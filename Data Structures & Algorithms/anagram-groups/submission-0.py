class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hashmap of the sorted word: words in strs
        hmap = {}

        #go through each word in the list
        for s in strs:
            #initialize x to each word sorted (nat,tan ->sorted-> ant)
            x = "".join(sorted(s))
            #append original word to hashmap 
            if x in hmap:
                hmap[x].append(s)
            else:
                hmap[x] = [(s)]
        return list(hmap.values())

            




        