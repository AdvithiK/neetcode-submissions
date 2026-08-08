class Solution:
    def isValid(self, s: str) -> bool:
        #a stack to take in half the input
        stack = []

        #dictionary to store matching pairs
        pairs = {")":"(", "]":"[", "}":"{"}

        #loop through to add the L parenthesis & pop the R parenthesis 
        for i in s:
            if i in pairs:
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        
        #if stack is empty, it was in correct order, else false
        if not stack:
            return True
        else:
            return False

        