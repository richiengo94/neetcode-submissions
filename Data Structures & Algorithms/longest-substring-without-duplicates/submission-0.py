class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len: int = 0
        l_ptr: int = 0
        r_ptr: int = 0

        while r_ptr < len(s):

            if s[r_ptr] in s[l_ptr:r_ptr]:
                l_ptr += 1
            else:
                max_len = max(max_len, r_ptr - l_ptr + 1)
                r_ptr += 1

        return max_len