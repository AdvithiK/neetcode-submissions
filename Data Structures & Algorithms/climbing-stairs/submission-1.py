class Solution:
    def climbStairs(self, n: int) -> int:
        #fibonacci sequence Fn = Fn-1 + Fn-2, where Fn+1 = answer
        #initial condition: f0=1, f1 = 1
        f0, f1 = 1, 1
        #until we reach n, iteratively add
        for i in range(n-1):
            #store one previous value
            temp = f1
            #get the addition of the two values
            f1 = f1 + f0
            #restore one previous so that new value gets added next iter
            f0 = temp
        return f1
        




        