class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort()

        while cars:
            pos, speed = cars.pop()
            time = (target - pos) / speed
            if not stack or stack[-1] < time:
                stack.append(time) 
        
        return len(stack)


        