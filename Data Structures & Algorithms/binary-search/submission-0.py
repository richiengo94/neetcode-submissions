class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_ptr: int = 0
        r_ptr: int = len(nums) - 1

        while l_ptr <= r_ptr:
            midpoint: int = (r_ptr + l_ptr) // 2
            if target < nums[midpoint]:
                r_ptr = midpoint - 1
            elif target > nums[midpoint]:
                l_ptr = midpoint + 1
            else:
                return midpoint
        
        return -1