class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        else:
            set_nums = set([])
            for i in nums:
                if i not in set_nums:
                    set_nums.add(i)
                else:
                    return True

            return False