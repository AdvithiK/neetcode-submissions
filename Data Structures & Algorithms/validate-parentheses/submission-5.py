class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dict = {')':'(',']':'[','}':'{'}

        for i in s:
            if i in dict:
                if stack and stack[-1] == dict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        return len(stack) == 0
        