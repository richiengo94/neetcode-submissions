class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k: int = k
        self.nums_list: list[int] = nums

    def add(self, val: int) -> int:
        self.nums_list.append(val)

        nums_heap: list = []
        for num in self.nums_list:
            heapq.heappush(nums_heap, num)

            if len(nums_heap) > self.k:
                heapq.heappop(nums_heap)

        return nums_heap[0]