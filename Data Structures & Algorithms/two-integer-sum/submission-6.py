class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict: dict[list[int, int]] = {}

        for idx, ele in enumerate(nums):
            nums_dict.update({ele: idx})
            
        for idx, ele in enumerate (nums):
            remainder: int = target - ele
            
            if nums_dict.get(remainder) and idx != nums_dict.get(remainder):
                return [idx, nums_dict.get(remainder)]