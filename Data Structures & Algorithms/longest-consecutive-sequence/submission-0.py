class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #turn into set for easy lookup
        numSet = set(nums)
        longest = 0
        
        #loop through array and check for one lower & one higher
        for n in nums:
            #if one lower exists, it's the start of a sequence 
            if (n - 1) not in numSet:
                #n is not at the start of sequence
                length = 0
                #while one higher than previous number exists, increase length of sequence
                while(n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


        