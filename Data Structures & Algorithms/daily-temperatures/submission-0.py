class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[List[int, int]] = []
        result: List[int] = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popped: int = stack.pop()
                stack_temp: int = popped[0]
                stack_idx: int = popped[1]
                result[stack_idx] = idx - stack_idx
                
            stack.append([temp, idx])

        return result