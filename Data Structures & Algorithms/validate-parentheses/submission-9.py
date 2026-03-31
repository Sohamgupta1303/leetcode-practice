class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = [')', ']', '}']
        opening = ['(', '[', '{']
        for i in range(len(s)):
            char = s[i]
            if char in close:
                index = close.index(char)
                if len(stack) == 0:
                    return False
                elif stack.pop() == opening[index]:
                    continue
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0

        