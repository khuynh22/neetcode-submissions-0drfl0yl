class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_res = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            anagram_res[sorted_str].append(s)

        return list(anagram_res.values())
        