class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if (len(stack) != 0):
                while len(stack) != 0:
                    stack_pair = stack[-1]
                    if temperatures[i] > stack_pair[0]:
                        stack.pop()
                        index = stack_pair[1]
                        result[index] = i - index
                    else:
                        break
            stack.append((temperatures[i], i))
        
        return result

                
