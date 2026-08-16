class Solution:
    def climbStairs(self, n: int) -> int:
        #fibonacci sequence Fn = Fn-1 + Fn-2, where Fn+1 = answer
        #use Binet's formula to calculate the Fibonacci value

        #binet's formula is (phi^n - psi^n)/2
        
        #import sqrt5 from math library

        sqrt5 = math.sqrt(5)
        #since fn+1 = answer, increment n by 1
        n+=1
        #calculate phi & psi
        phi = ((1+sqrt5)/2)**n
        psi = ((1-sqrt5)/2)**n

        answer = round((phi-psi)/ sqrt5)
        return answer


        