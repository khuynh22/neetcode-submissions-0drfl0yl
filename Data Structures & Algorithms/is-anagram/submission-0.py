class Solution:
    def _occurence_hash(self, s: str) -> dict[str, int]:
        res = {}
        for c in s:
            if c in res:
                res[c] += 1
            else:
                res[c] = 1
        return res

    def isAnagram(self, s: str, t: str) -> bool:
        return self._occurence_hash(s) == self._occurence_hash(t)
        