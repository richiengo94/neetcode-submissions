class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_ptr: int = 0
        r_ptr: int = len(nums) - 1
        
        while l_ptr <= r_ptr:
            mid: int = (l_ptr + r_ptr) // 2

            if target > nums[mid]:
                l_ptr = mid + 1

            elif target < nums[mid]:
                r_ptr = mid - 1
            
            else:
                return mid

        return -1