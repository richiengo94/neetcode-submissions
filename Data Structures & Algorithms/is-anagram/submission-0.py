from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter()
        t_counter = Counter()
        for i in s:
            s_counter[i] += 1
        for i in t:
            t_counter[i] += 1

        return s_counter == t_counter