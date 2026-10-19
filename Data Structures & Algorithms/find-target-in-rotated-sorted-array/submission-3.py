class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_ptr: int = 0
        r_ptr: int = len(nums) - 1

        while l_ptr <= r_ptr:
            mid: int = (l_ptr + r_ptr) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l_ptr] <= nums[mid]:
                if target > nums[mid] or target < nums[l_ptr]:
                    l_ptr = mid + 1
                else:
                    r_ptr = mid - 1
            else:
                if target < nums[mid] or target > nums[r_ptr]:
                    r_ptr = mid - 1
                else:
                    l_ptr = mid + 1

        return -1