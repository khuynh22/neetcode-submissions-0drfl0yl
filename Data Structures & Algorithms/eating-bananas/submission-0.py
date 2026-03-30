class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            total_t = 0
            for p in piles:
                total_t += math.ceil(p/k)
            if total_t > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res
