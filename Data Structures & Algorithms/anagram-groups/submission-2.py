from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: defaultdict = defaultdict(list)

        for word in strs:
            sorted_txt: str = ''.join(sorted(word))
            result[sorted_txt].append(word)
        return list(result.values())