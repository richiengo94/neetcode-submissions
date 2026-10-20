class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: list[list[int]] = []
        nums.sort()

        for idx, ele in enumerate(nums):
            if ele > 0:
                break
            
            if idx > 0 and ele == nums[idx - 1]:
                continue

            l_ptr: int = idx + 1
            r_ptr: int = len(nums) - 1

            while l_ptr < r_ptr:
                total = ele + nums[l_ptr] + nums[r_ptr]
                if total > 0:
                    r_ptr -= 1
                elif total < 0:
                    l_ptr += 1
                else:
                    result.append([ele, nums[l_ptr], nums[r_ptr]])
                    l_ptr += 1
                    r_ptr -= 1
                    while nums[l_ptr] == nums[l_ptr - 1] and l_ptr < r_ptr:
                        l_ptr += 1

        return result