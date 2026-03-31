class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def helper(parenthesis: str, opened: int, closed: int):
            if opened == closed == n:
                ret.append(parenthesis)
                return
            
            # first case, when we decide to opened a bracket
            if (opened < n):
                helper(parenthesis + "(", opened + 1, closed)
            
            if (closed < opened):
                helper(parenthesis + ")", opened, closed + 1)
        
        helper("", 0, 0)
        return ret

