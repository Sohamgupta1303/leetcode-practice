class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heap = stones
        heapq.heapify(stones)

        while(len(heap) > 1):
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            result = min(first, second) - max(first, second)
            heapq.heappush(heap, result)
        
        return heapq.heappop(heap) * -1