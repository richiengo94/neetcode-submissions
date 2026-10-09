class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l_ptr: int = 0
        r_ptr: int = len(numbers) -  1

        while l_ptr < r_ptr:
            if numbers[l_ptr] + numbers[r_ptr] > target:
                r_ptr -= 1
            elif numbers[l_ptr] + numbers[r_ptr] < target:
                l_ptr += 1
            else:
                return [l_ptr + 1, r_ptr + 1]