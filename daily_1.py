class Solution(object):
    def makeGood(self, s):
        stack = []
        for char in s:
            if stack and stack[-1] == char.swapcase():
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
                    

            
