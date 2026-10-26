class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_ptr: int = 0
        bot_ptr: int = len(matrix) - 1

        while top_ptr <= bot_ptr:
            mid_row: int = (top_ptr + bot_ptr) // 2

            if target > matrix[mid_row][-1]:
                top_ptr = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot_ptr = mid_row - 1
            else:
                break

        if top_ptr > bot_ptr:
            return False

        curr_row: int = (top_ptr + bot_ptr) // 2
        l_ptr: int = 0
        r_ptr: int = len(matrix[curr_row]) - 1

        while l_ptr <= r_ptr:
            mid_col: int = (l_ptr + r_ptr) // 2

            if target == matrix[curr_row][mid_col]:
                return True
            elif target > matrix[curr_row][mid_col]:
                l_ptr = mid_col + 1
            else:
                r_ptr = mid_col - 1

        return False