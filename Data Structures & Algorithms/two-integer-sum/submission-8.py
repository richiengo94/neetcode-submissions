class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums: dict = dict([])

        for idx, ele in enumerate(nums):
            dict_nums[ele] = idx
        
        print(dict_nums)

        for idx, ele in enumerate(nums):
            if target - ele in dict_nums and idx != dict_nums.get(target - ele):
                return [idx, dict_nums.get(target - ele)]