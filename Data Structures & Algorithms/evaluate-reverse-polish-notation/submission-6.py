class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                result = 0
                if (token == '+'):
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    stack.append(int(num2 / num1))
                print(stack[-1])

        return stack.pop()


        