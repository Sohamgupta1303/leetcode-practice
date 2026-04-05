class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)

            recent_interval = stack[-1]
            if (interval[0] >= recent_interval[0] and interval[0] <= recent_interval[1]):
                stack.pop()
                stack.append([recent_interval[0], max(interval[1], recent_interval[1])])
            
            if interval[0] > stack[-1][1]:
                stack.append(interval)
        
        return stack





            
        