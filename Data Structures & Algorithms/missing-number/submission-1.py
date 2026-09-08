class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #using bitwise XOR for O(1) space
        n = len(nums)
        xorr = n
        #XOR i with nums[i], if same then == 0, else returns i
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr


        