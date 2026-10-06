class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result: List[int] = []
        
        if len(nums) == 2:
            return [0, 1]

        for idx, ele in enumerate(nums):
            remainder: int = target - ele
            
            if remainder in nums[idx + 1:]:
                result.append(idx)
            else:
                if result:
                    if nums[result[0]] + ele == target:
                        result.append(idx)

        return result