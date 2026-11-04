class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            largest_stone: int = heapq.heappop_max(stones)
            second_stone: int = heapq.heappop_max(stones)
            if largest_stone != second_stone:
                largest_stone -= second_stone
                heapq.heappush_max(stones, largest_stone)

        return heapq.heappop_max(stones) if stones else 0