from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for idx, ele in enumerate(strs):
            sorted_txt = ''.join(sorted(ele))
            result[sorted_txt].append(ele)
        return list(result.values())