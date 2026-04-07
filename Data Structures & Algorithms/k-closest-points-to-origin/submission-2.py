class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            eu_distance = (point[0] ** 2 + point[1] ** 2) ** .5
            heap.append((eu_distance, point[0], point[1]))
        
        ret = []
        heapq.heapify(heap)
        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            ret.append([x, y])
        
        return ret
        

        