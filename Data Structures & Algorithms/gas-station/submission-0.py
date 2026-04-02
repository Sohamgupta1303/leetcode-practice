class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
        if total_cost > total_gas:
            return -1

        # we need to find the first index from where on out the sum is positive
        sum = 0
        index = 0
        for i in range(len(gas)):
            if sum == 0:
                index = i
            sum += (gas[i] - cost[i])
            if sum < 0:
                sum = 0

        return index
            
        

        