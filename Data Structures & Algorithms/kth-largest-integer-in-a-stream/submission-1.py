class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k: int = k
        self.nums: list[int] = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            if val > self.nums[0]:
                heapq.heapreplace(self.nums, val)

        return self.nums[0]