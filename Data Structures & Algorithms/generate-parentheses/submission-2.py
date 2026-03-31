class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        stack = []

        def helper(opened: int, closed: int):
            if opened == closed == n:
                ret.append("".join(stack))
                return
            
            # first case, when we decide to opened a bracket
            if (opened < n):
                stack.append("(")
                helper(opened + 1, closed)
                stack.pop()
            
            if (closed < opened):
                stack.append(")")
                helper(opened, closed + 1)
                stack.pop()
        
        helper(0, 0)
        return ret

