class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        #bitwise shift 
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31-i))
        return res


        