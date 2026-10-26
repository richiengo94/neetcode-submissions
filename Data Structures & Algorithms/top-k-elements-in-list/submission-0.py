class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        min_heap = []
        for num in count.keys():
            heapq.heappush(min_heap, (count[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result: list[int] = []
        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])

        return result