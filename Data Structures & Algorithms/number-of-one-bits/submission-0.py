class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        #assuming all integers are represented in 32 bits
        while n:
            #use & operation to move the bit and check for 1
            n &= n - 1
            res += 1
        return res
        